from django.contrib import admin
from .models import Post, Structure, Player, NbaTeam, RookieDraftStyle, RegSeasonDraftStyle

admin.site.register(Post)
admin.site.register(Structure)


class PlayerInfoAdmin(admin.ModelAdmin):
    list_display = ('player_full',
                    'player_owner',
                    'id',
                    'player_position',
                    'player_nba_team',
                    'player_sal_19_20',
                    'player_sal_20_21',
                    'player_sal_21_22',
                    'player_sal_22_23'
                    )

    def player_info(self, obj):
        return obj.description


admin.site.register(Player, PlayerInfoAdmin)
admin.site.register(NbaTeam)
admin.site.register(RookieDraftStyle)
admin.site.register(RegSeasonDraftStyle)
