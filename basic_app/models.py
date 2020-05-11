from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user=models.OneToOneField(User)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics', blank=True)#ne pas oublier de creer profile_pic directory sous media!

    def  __str__(self):
        return self.user.username
