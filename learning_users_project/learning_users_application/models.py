from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfor(models.Model):
    user = models.OneToOneField(User)
#Users additional attributes/ custom user attributes
    portfolio_site = models.URLField(blank=True)# blank = true means a user can leave this field empty
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self): 
        return self.user.username
