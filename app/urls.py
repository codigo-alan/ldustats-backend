from rest_framework import routers
from django.urls import path, include
from app import views


router = routers.DefaultRouter()
router.register(r'players', views.PlayerView, 'players') 
router.register(r'sessions', views.SessionView, 'sessions') 

urlpatterns = [ 
    path("api/v1/", include(router.urls))
]