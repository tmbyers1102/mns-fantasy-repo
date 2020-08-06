from rest_framework import serializers
from .models import Player


class playerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('player_full',
                  'c_week_fg_per',
                  'c_week_ft_per',
                  'c_week_3pm',
                  'c_week_reb',
                  'c_week_ast',
                  'c_week_ato',
                  'c_week_stl',
                  'c_week_blk',
                  'c_week_pts',
                  )
