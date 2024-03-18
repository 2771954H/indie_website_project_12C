"""indie urls file"""

from django.urls import path
from indie import views

app_name = "indie"

urlpatterns = [
    path("", views.index, name="index"),
    path("game/<slug:game_name_slug>/", views.show_game, name="show_game"),
    path("dev_home/", views.dev_home, name="dev_home"),
    path("upload_game/", views.upload_game, name="upload_game"),
    path("logout/", views.logout, name="logout"),
    path("register", views.register, name = "register"),
    path('login/', views.user_login, name = 'login')
]
