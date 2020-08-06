from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib import messages
from .models import Player, NbaTeam


class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['player_owner']

    def clean(self):
        if self.request.method == 'POST':
            form = AddPlayerForm(self.request.POST)
            form.save(commit=False)
            current_user = self.request.user
            if Player.objects.filter(player_owner=current_user).count() <= 14:
                pass
            else:
                raise ValidationError('Your team is full!')
