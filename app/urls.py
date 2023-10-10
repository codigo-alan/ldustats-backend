from rest_framework import routers
from django.urls import path, include
from app import views


router = routers.DefaultRouter()
router.register(r'players', views.PlayerView, 'players') 
router.register(r'sessions', views.SessionView, 'sessions') 
router.register(r'files', views.FileView, 'files') 
router.register(r'players/(?P<id>\w+)/sessions', views.SessionByPlayerView, 'sessions') #verify 3rd param (basename)
router.register(r'files-filters', views.FilesByIdsView, 'files')
router.register(r'register', views.RegisterUserView, 'register') #not works

urlpatterns = [ 
    path("api/v1/", include(router.urls))
]
