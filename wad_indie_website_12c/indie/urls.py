"""indie urls file"""

from django.urls import path
from indie import views

app_name = "indie"

urlpatterns = [
    path("", views.index, name="index"),
    path("game/<slug:game_name_slug>/", views.show_game, name="show_game"),
    path("user/<slug:username>/", views.show_user, name="show_user"),
    path("search/", views.search, name="search"),
    path("dev_home/", views.dev_home, name="dev_home"),
    path("upload_game/", views.upload_game, name="upload_game"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register", views.register, name="register"),
    path("paypal/<slug:game_name_slug>", views.paypal, name="paypal"),
    path("like_game/", views.like_game, name="like_game"),
]
