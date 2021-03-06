"""training_wheels_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('my_games/', views.game_list, name='my_games'),
    path('available_games/', views.available_game_list, name='available_games'),
    path('create_new_game/', views.create_new_game_with_model_form, name='create_new_game'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('game/<int:game_id>/', views.game_view, name='game_view'),
    path('game/<int:game_id>/join/', views.join_game_view, name='join_game_view'),
]
