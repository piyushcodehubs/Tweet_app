from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('make-tweet/', views.make_tweet, name="make_tweet"),
    
]
