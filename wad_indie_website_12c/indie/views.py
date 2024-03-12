from django.shortcuts import render
from django.http import HttpResponse

from indie.models import Game


def index(request):
    context_dict = {}
    context_dict["pagename"] = "Index"
    games_list = Game.objects.order_by("-likes")[:4]
    context_dict["games"] = games_list
    return render(request, "indie/index.html", context=context_dict)


def logout(request):
    return index(request)


# Dev pages
def dev_home(request):
    context_dict = {}
    context_dict["pagename"] = "Dev Home"

    return render(request, "indie/dev_home.html", context=context_dict)


def upload_new_game(request):
    context_dict = {}
    context_dict["pagename"] = "Upload New Game"

    return HttpResponse("Uploading Your Game, Yay!")
