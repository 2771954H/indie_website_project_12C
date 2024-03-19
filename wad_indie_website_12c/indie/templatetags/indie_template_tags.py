from django import template
from indie.models import Game

register = template.Library()


@register.inclusion_tag("indie/games.html")
def get_games_list(games=None):
    return {"games": games}


@register.inclusion_tag("indie/devs.html")
def get_devs_list(devs=None):
    return {"devs": devs}
