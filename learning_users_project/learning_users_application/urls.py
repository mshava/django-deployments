from django.conf.urls import url
from learning_users_application import views

app_name = 'learning_users_application'

urlpatterns = [
    url(r'^register/$', views.register,name='register'),
    url(r'^user_login/$', views.user_login,name='user_login')
]
