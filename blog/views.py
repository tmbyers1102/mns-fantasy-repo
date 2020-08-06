from django.contrib.admin.templatetags.admin_list import register
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms
from django.contrib import messages
from django.db.models import Sum, Count
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.http import JsonResponse, HttpResponse
from .forms import AddPlayerForm
from .models import Post, Player

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import playerSerializer
import requests

import json


def stats(request):
    # api_url = 'https://api.sportsdata.io/v3/nba/stats/json/'
    # api_cat = 'PlayerGameStatsByDate'
    # api_date = '2018-DEC-01'
    # api_key = '538d702759d440029e450288b743e50b'
    # r = requests.get(api_url + api_cat + '/' + api_date + '?key=' + api_key).json()
    url = 'https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByDate/2018-DEC-01?key=538d702759d440029e450288b743e50b'

    r = requests.get(url).json()

    player_stats = {
        'rebounds': r['Rebounds']
    }

    print(player_stats)

    return render(request, 'blog/players.html')


class playerStatList(APIView):

    def get(self, request):
        players1 = Player.objects.all()
        serializer = playerSerializer(players1, many=True)
        return Response(serializer.data)

# https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByDate/%7Bdate%7D?key=538d702759d440029e450288b743e50b
# https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByDate/2018-DEC-01
# required data format = 2018-DEC-01
    def post(self, request):
        api_url = 'https://api.sportsdata.io/v3/nba/stats/json/'
        api_cat = 'PlayerGameStatsByDate'
        api_date = '2018-DEC-01'
        api_key = '538d702759d440029e450288b743e50b'
        r = requests.get(api_url + api_cat + '/' + api_date + '?key=' + api_key)
        json_object = r.text
        return json_object





posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post',
        'content': 'first post content',
        'date_posted': 'august 27th, 2018',
        'test': 'test item 1'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'august 28th, 2018',
        'test': 'test item 2'
    }
]


def home(request):
    url = 'https://api.sportsdata.io/v3/nba/scores/json/teams'
    api_key = '538d702759d440029e450288b743e50b'
    json_result = requests.get(url + '?key=' + api_key)

    data = json.load(json_result)
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'blog/about.html', context, {
        'city': data.get('LeagueID'),
        'name': data.get('TeamID')
    })


class UserListView(ListView):
    template_name = 'blog/base.html'
    model = User
    context_object_name = 'users'
    queryset = User.objects.all()


def user_list(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'blog/base.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ''' by default, django doesnt know what this variable should be named in our template
    that will be looping over. it default thinks its called 'object_list' but we have been calling
    the blog posts 'posts' (see def home) so this 'context_object_name' switches django to call it 'posts'
    '''
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ''' by default, django doesnt know what this variable should be named in our template
    that will be looping over. it default thinks its called 'object_list' but we have been calling
    the blog posts 'posts' (see def home) so this 'context_object_name' switches django to call it 'posts'
    '''
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # this def tells the new post that we want to use the current singed in user as author
    def form_valid(self, form):
        form.instance.author = self.request.user
        # and since the line above ^ overrides the validation, this next line re-validates
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # from video part 10 (32:30 min) this whole class copied from above PostCreateView class
    # this def tells the new post that we want to use the current singed in user as author
    def form_valid(self, form):
        form.instance.author = self.request.user
        # and since the line above ^ overrides the validation, this next line re-validates
        return super().form_valid(form)

    # this def makes sure only the post author can edit the post
    def test_func(self):
        # this makes sure it is the exact post we are updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # after you delete a post this -as required- sends user back to homepage
    success_url = '/'

    # copied from above PostUpdateView
    # this def makes sure only the post author can edit the post
    def test_func(self):
        # this makes sure it is the exact post we are updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    data = {
        'players': Player.objects.all()
    }
    return render(request, 'blog/about.html', data)


def players(request):

    context = {
        'players': Player.objects.all(),
    }
    return render(request, 'blog/players.html', context)


def player_update(request, id,):
    player = Player.objects.get(id=id)
    current_user = request.user
    if Player.objects.filter(player_owner=current_user).count() <= 14:
        player.player_owner = current_user
        player.save()
        messages.success(request, f'Player added!')
        return redirect('blog-players')
    else:
        messages.warning(request, f'Your roster is full! Player not added.')
        return redirect('blog-players')


class PlayersListView(ListView):
    model = Player
    template_name = 'blog/players.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'players'
    ''' by default, django doesnt know what this variable should be named in our template
    that will be looping over. it default thinks its called 'object_list' but we have been calling
    the blog posts 'posts' (see def home) so this 'context_object_name' switches django to call it 'posts'
    '''
    ordering = ['-player_sal_19_20']
    paginate_by = 800


class PlayersDetailView(DetailView):
    model = Player


class PlayersCreateView(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['player_full',
              'player_first',
              'player_last',
              'player_position',
              'player_nba_team',
              'player_owner'
              ]

    def form_valid(self, form):
        ''' the commented out below ensures when a player is created on front end their assigned player_owner
        is automatically the signed-in user. this is not good for player add/drop since we want to assign
        all new players as FA's. also, we dont want to create new players on front end.
        we just had to make this view in order to create
        the functionality of the playersupdateview which allows player add/drop
        * maybe consider uncommenting this and change self.request.user to "Free_Agent"?
        '''
        # form.instance.player_owner = self.request.user
        return super().form_valid(form)


class PlayersDropView(LoginRequiredMixin, UpdateView):
    model = Player
    fields = []
    template_name = 'blog/players_drop.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'players'

    # this def makes sure only the post author can edit the post
    def test_func(self):
        # this makes sure it is the exact post we are updating
        player = self.get_object()
        if self.request.user == player.player_owner:
            return True
        return False

    def form_valid(self, form):
        form.instance.player_owner = None
        return super().form_valid(form)


class PlayersUpdateView(LoginRequiredMixin, UpdateView, Player):
    model = Player
    fields = ['player_full', 'player_owner']
    template_name = 'blog/player_form.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'players'
    form = AddPlayerForm()

    # this def makes sure only the post author can edit the post
    def test_func(self, **kwargs):
        # this makes sure it is the exact post we are updating
        player = self.get_object()
        if self.request.user == player.player_owner:
            return True
        return False

    def form_valid(self, form):
        form = AddPlayerForm(self.request.POST)
        form.instance.player_owner = self.request.user
        return super().form_valid(form)

'''
    def form_valid(self, form):
        if self.request.method == 'POST':
            form = AddPlayerForm(self.request.POST)
            if form.is_valid():
                form.save(commit=False)
                current_user = self.request.user
                if Player.objects.filter(player_owner=current_user).count() > 14:
                    # do something here, such as return error or redirect to another page
                    messages.warning(self.request, f'Your roster is full! Player not added.')
                    return redirect('profile')
                    # raise ValidationError('Your team is full!')
                else:
                    form.instance.player_owner = self.request.user
                    return super().form_valid(form)
'''

'''
# i commented this out so a user (not signed in as FA can 'update' aka re-assign the player_owner to
# their team aka add player. this def is used in other classes to make sure users can only adjust their
# own players. Aka this leaves us vulnerable to url attacks but views wont be there. must make
# PlayersUpdateView have one function: change player_owner from only Free_Agent to whatever user is
# signed in
    def test_func(self):
        player = self.get_object()
        if self.request.user == player.player_owner:
            return True
        return False
'''


class UserPlayerListView(ListView):
    model = Player
    template_name = 'blog/user_players.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'players'
    ''' by default, django doesnt know what this variable should be named in our template
    that will be looping over. it default thinks its called 'object_list' but we have been calling
    the blog posts 'posts' (see def home) so this 'context_object_name' switches django to call it 'posts'
    '''
    paginate_by = 20
    # ordering = ['-player_sal_19_20']

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'blog/user_players.html', {})

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Player.objects.filter(player_owner=user).order_by('-player_sal_19_20')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player_list = list(context['players'])  # evaluates the query
        context['sum_of_sal_19_20'] = sum([x.player_sal_19_20 for x in player_list])  # pythonic sum calculation
        context['sum_of_sal_20_21'] = sum([x.player_sal_20_21 for x in player_list])
        context['sum_of_sal_21_22'] = sum([x.player_sal_21_22 for x in player_list])
        context['sum_of_sal_22_23'] = sum([x.player_sal_22_23 for x in player_list])
        context['player_count'] = sum([x.player_unit_value for x in player_list])
        context['players'] = player_list
        return context


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'user_players.html', {})


def get_data(request, *args, **kwargs):
    url = 'https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByDate/2018-DEC-01?key=538d702759d440029e450288b743e50b'

    r = requests.get(url).json()

    player = Player.objects.filter(player_owner_id=1)
    data = {
        "sales": 100,
        "customers": 10,
        "other": [user.username for user in User.objects.all()],
        "player_names": [player.player_full for player in player],
        "player_sals": [player.player_sal_19_20 for player in player],
        "rebounds": [r[2]]
    }
    return JsonResponse(data) # http response


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        player = Player.objects.filter(player_owner_id=1)
        free_agents = Player.objects.filter(player_owner_id=None)[:10]
        labels = [player.player_full for player in player]
        default_items = [player.player_sal_19_20 for player in player]
        data_20_21 = [player.player_sal_20_21 for player in player]
        data_21_22 = [player.player_sal_21_22 for player in player]
        data_22_23 = [player.player_sal_22_23 for player in player]
        fa_bubble_data = [player.player_sal_19_20 for player in free_agents]
        fa_bubble_labels = [player.player_full for player in free_agents]
        data = {
            "labels": labels,
            "default": default_items,
            "data_20_21": data_20_21,
            "data_21_22": data_21_22,
            "data_22_23": data_22_23,
            "fa_bubble_data": fa_bubble_data,
            "fa_bubble_labels": fa_bubble_labels,
        # "other": [user.username for user in User.objects.all()],
            # "player_names": [player.player_full for player in player],
            # "player_sals": [player.player_sal_19_20 for player in player]
        }
        return Response(data)



"""
stack 3rd method -- could not get this to work, but the guy said it was the best option of the three
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players_salary_values = list(
            context['players'].values('player_owner').annotate(
                sum_of_sal_19_20=Sum('player_sal_19_20'),
                sum_of_sal_20_21=Sum('player_sal_20_21'),
                sum_of_sal_21_22=Sum('player_sal_21_22'),
                sum_of_sal_22_23=Sum('player_sal_22_23')
            ).values(
                'sum_of_sal_19_20',
                'sum_of_sal_20_21',
                'sum_of_sal_21_22',
                'sum_of_sal_22_23'
            )
        )[0]
        # as there is only one player owner here, you can use 1st index of the list
        context.update(players_salary_values)
        return context


original stack overflow method

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_of_sal_19_20'] = context['players'].aggregate(players_sum=Sum('player_sal_19_20'))['players_sum']
        context['sum_of_sal_20_21'] = context['players'].aggregate(players_sum=Sum('player_sal_20_21'))['players_sum']
        context['sum_of_sal_21_22'] = context['players'].aggregate(players_sum=Sum('player_sal_21_22'))['players_sum']
        context['sum_of_sal_22_23'] = context['players'].aggregate(players_sum=Sum('player_sal_22_23'))['players_sum']
        return context

"""


