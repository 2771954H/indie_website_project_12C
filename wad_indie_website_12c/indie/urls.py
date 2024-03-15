"""indie urls file"""

from django.urls import path
from indie import views

# working app_name-honestly would be easy to just stick to it
app_name = "indie"

urlpatterns = [
    path("", views.index, name="index"),
    path("game/<slug:game_name_slug>/", views.show_game, name="show_game"),
    path("dev_home/", views.dev_home, name="dev_home"),
    path("upload_game/", views.upload_game, name="upload_game"),
    path("logout", views.logout, name="logout"),
]
