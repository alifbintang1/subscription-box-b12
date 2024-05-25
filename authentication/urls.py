from django.urls import path
from authentication.views import register, login, logout_user

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout_user'),
]