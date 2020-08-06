from django import template
from ..models import Player
from django.template import Library

register = Library()





'''
@register.filter(name='sum_of_sal')
def return_item(self):

    total_sum = Player.objects.filter(player_owner__exact=self).aggregate(Sum('player_sal_19_20'))
    return
    
def get_team_sal(sal):
    team_sal = {}
    for Player 
    
@register.filter
def running_total(fine_list):
    return sum(d.get())
    
'''

