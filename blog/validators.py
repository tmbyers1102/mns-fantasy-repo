from django.core.exceptions import ValidationError


def validate_roster_max(value):
    value = super().get_context_data(**kwargs)
    player_list = list(value['object_list'])  # evaluates the query
    value['player_count'] = sum([x.player_unit_value for x in player_list])
    value['object_list'] = player_list
    if value['player_count'] > 15:
        raise ValidationError(u'max roster message')

