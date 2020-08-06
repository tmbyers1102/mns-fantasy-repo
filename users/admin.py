from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'players_owned']

    def profile_info(self, obj):
        return obj.description


admin.site.register(Profile, ProfileAdmin)