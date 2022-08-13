from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_view, name='home_view'),
    path('user', views.user_view, name='user_view')
]