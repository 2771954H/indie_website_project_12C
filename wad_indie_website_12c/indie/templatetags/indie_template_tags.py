from django import template
from indie.models import Game

register = template.Library()


@register.inclusion_tag("indie/games.html")
def get_games_list(games=None):
    return {"games": games}
