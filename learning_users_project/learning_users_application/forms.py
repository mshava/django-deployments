from django import forms
from django.contrib.auth.models import User
from learning_users_application.models import UserProfileInfor

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInforForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfor
        fields = ('portfolio_site', 'profile_pic')
