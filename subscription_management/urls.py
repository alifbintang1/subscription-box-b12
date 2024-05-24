from django.urls import include, path
from . import views

app_name = 'subscription_management'

urlpatterns = [
    path('', views.box_list, name='box_list'),
    path('<int:box_id>/', views.box_detail, name='box_detail'),
    path('history/', views.subscription_history, name='subscription_history'),

    path('fetch_boxes/', views.fetch_boxes, name='fetch_boxes')
    
]