from django.shortcuts import render
from django.http import HttpResponse

from indie.models import Game


def index(request):
    context_dict = {}
    context_dict["pagename"] = "Index"
    featured_games_list = Game.objects.filter(featured=True)[:4]
    popular_games_list = Game.objects.order_by("-downloads")[:4]
    new_games_list = Game.objects.order_by("-upload_date")[:4]
    top_games_list = Game.objects.order_by("-likes")[:4]
    context_dict["featured_games"] = featured_games_list
    context_dict["popular_games"] = popular_games_list
    context_dict["new_games"] = new_games_list
    context_dict["top_games"] = top_games_list
    return render(request, "indie/index.html", context=context_dict)


def show_game(request, game_name_slug):
    context_dict = {}

    try:
        game = Game.objects.get(slug=game_name_slug)
        context_dict["game"] = game
    except Game.DoesNotExist:
        context_dict["game"] = None

    return render(request, "indie/game_page.html", context=context_dict)


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
