"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from app.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ldustats/', include('app.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # with POST return a response with token
    path('api/token/refresh/', jwt_views.token_refresh, name='token_refresh'), # with POST return a response to refresh token
]
