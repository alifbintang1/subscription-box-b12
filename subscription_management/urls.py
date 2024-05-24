from django.urls import include, path
from . import views

app_name = 'subscription_management'

urlpatterns = [
    path('', views.subscription_list, name='subscription_list'),
    path('<int:subscription_id>/', views.subscription_detail, name='subscription_detail'),
    path('history/', views.subscription_history, name='subscription_history'),
]