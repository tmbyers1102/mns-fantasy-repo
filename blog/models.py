from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from django.core.exceptions import ValidationError


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # how do we want the data to be printed out?
    # when we need to adjust/update these models go to
    # https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5
    # around 19 or 20 min mark
    def __str__(self):
        return self.title

    # this def makes it so it properly re-direct aka reverse to post url after submitting created post
    # if you wanted it to redirect to home instead, you'd have to set attribute in views.py PostCreateView
    # called success_url and set to home page (video does not do this method)
    # video part 10 (min 30 ish)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Structure(models.Model):
    league_id = models.CharField(max_length=100)
    league_name = models.CharField(max_length=100)
    league_style = models.CharField(max_length=100)
    players_per_team = models.IntegerField()
    league_bit_wallet_1 = models.URLField(blank=True, null=True)
    league_bit_wallet_2 = models.URLField(blank=True, null=True)
    league_node_1 = models.URLField(blank=True, null=True)
    league_node_2 = models.URLField(blank=True, null=True)
    teams_amount = models.IntegerField()
    #cap = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    structure_cap = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    #hard_cap = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    structure_hard_cap = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    lux_tax_per = models.IntegerField()
    reg_season_draft_date = models.DateTimeField()
    rookie_draft_date = models.DateTimeField()
    eligible_draft_pick_timeframe = models.DateTimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    # out of box django group = fantasy team and fantasy league
    rook_draft_style = models.ForeignKey("RookieDraftStyle",
                                         blank=True,
                                         null=True,
                                         on_delete=models.CASCADE)
    regular_draft_style = models.ForeignKey("RegSeasonDraftStyle",
                                         blank=True,
                                         null=True,
                                         on_delete=models.CASCADE)

    # how do we want the data to be printed out?
    def __str__(self):
        return self.league_name


class NbaTeam(models.Model):
    TeamID = models.PositiveSmallIntegerField(null=True)
    Key = models.CharField(blank=True, null=True, max_length=4)
    Active = models.BooleanField()
    City = models.CharField(blank=True, null=True, max_length=25)
    Name = models.CharField(blank=True, null=True, max_length=25)
    LeagueID = models.PositiveSmallIntegerField(null=True)
    StadiumID = models.PositiveSmallIntegerField(null=True)
    Conference = models.CharField(blank=True, null=True, max_length=25)
    Division = models.CharField(blank=True, null=True, max_length=25)
    PrimaryColor = models.CharField(blank=True, null=True, max_length=25)
    SecondaryColor = models.CharField(blank=True, null=True, max_length=25)
    TertiaryColor = models.CharField(blank=True, null=True, max_length=25)
    QuaternaryColor = models.CharField(blank=True, null=True, max_length=25)
    WikipediaLogoUrl = models.CharField(blank=True, null=True, max_length=200)
    GlobalTeamID = models.PositiveSmallIntegerField(null=True)
    NbaDotComTeamID = models.PositiveSmallIntegerField(null=True)

    def formalname(self):
        return '{} {}'.format(self.City, self.Name)

    def __str__(self):
        return self.formalname


class Player(models.Model):
    player_full = models.CharField(max_length=50)
    player_first = models.CharField(blank=True, null=True, max_length=50)
    player_last = models.CharField(blank=True, null=True, max_length=50)
    player_team = models.CharField(blank=True, null=True, max_length=100)
    player_position = models.CharField(blank=True, null=True, max_length=50)
    player_nba_team = models.CharField(blank=True, null=True, max_length=100)
    # player_salary = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    # player_sal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    player_sal_19_20 = models.IntegerField(default=0)
    player_sal_20_21 = models.IntegerField(default=0)
    player_sal_21_22 = models.IntegerField(default=0)
    player_sal_22_23 = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    # nba_team = models.ForeignKey("Nbateams", blank=True, null=True, on_delete=models.CASCADE)
    player_owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(default='default_player.jpg', upload_to='player_pics')
    # fa-status starts out as null by default, switches to False when a owner is assigned
    # and then switches to True if the owner is ever switched back to null
    player_unit_value = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1),
                                                                                MaxValueValidator(1),])
    two_point_perc = models.FloatField(default=0)
    c_week_fg_per = models.FloatField(default=0)
    c_week_ft_per = models.FloatField(default=0)
    c_week_3pm = models.PositiveSmallIntegerField(default=0)
    c_week_reb = models.PositiveSmallIntegerField(default=0)
    c_week_ast = models.PositiveSmallIntegerField(default=0)
    c_week_ato = models.FloatField(default=0)
    c_week_stl = models.PositiveSmallIntegerField(default=0)
    c_week_blk = models.PositiveSmallIntegerField(default=0)
    c_week_pts = models.PositiveSmallIntegerField(default=0)

    def fullname(self):
        return '{} {}'.format(self.player_first, self.player_last)

    # how do we want the data to be printed out?
    def __str__(self):
        return self.player_full

    def get_absolute_url(self):
        return reverse('players-detail', kwargs={'pk': self.pk})


class RookieDraftStyle(models.Model):
    rookie_draft_style = models.CharField(max_length=100)
    rookie_draft_style_desc = models.TextField(blank=True, null=True)

    def rookie_draft_comb(self):
        return '{}: {}'.format(self.rookie_draft_style, self.rookie_draft_style_desc)

    def __str__(self):
        return self.rookie_draft_comb()


class RegSeasonDraftStyle(models.Model):
    reg_draft_style = models.CharField(max_length=100)
    reg_draft_style_desc = models.TextField(blank=True, null=True)

    def reg_draft_comb(self):
        return '{}: {}'.format(self.reg_draft_style, self.reg_draft_style_desc)

    def __str__(self):
        return self.reg_draft_comb()
