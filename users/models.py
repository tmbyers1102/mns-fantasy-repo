from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    players_owned = models.PositiveSmallIntegerField(default=0,
                                                     validators=[MinValueValidator(0),
                                                                 MaxValueValidator(15)]
                                                     )

    def __str__(self):
        return f'{self.user.username}s Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



'''
    def formfield(self, **kwargs):
    return super().formfield(**{ min_value': 0, **kwargs,})
'''

