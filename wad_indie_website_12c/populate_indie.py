import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad_indie_website_12c.settings")

import django

django.setup()
from indie.models import Genre, Game, Feedback, UserProfile
from django.contrib.auth.models import User
from enum import Enum


def populate():

    class Genres(Enum):
        FARMING_SIMULATOR = 1
        PLATFORMER = 2
        ACTION_ADVENTURE = 3
        SURVIVAL_HORROR = 4
        RPG = 5
        FPS = 6
        RACING = 7
        FISHING_HORROR_SIMULATOR = 8
        HOLLOW_LIKE = 9

        def __str__(self):
            return self.name

    steve_games = [
        {"name": "Jumper of Planet S", "price": 30, "genre": Genres.FARMING_SIMULATOR},
        {"name": "Empty Sir for Dummies", "price": 15, "genre": Genres.HOLLOW_LIKE},
        {
            "name": "Crush those Pistachio Shells",
            "price": 150,
            "genre": Genres.FISHING_HORROR_SIMULATOR,
            "description": "Rip-off Candy Crush",
        },
    ]

    spindie_games = [
        {
            "name": "Destroyer of only one acre of land, its really not that big of a deal",
            "price": 0.5,
            "genre": Genres.ACTION_ADVENTURE,
        },
        {
            "name": "Destroyer of only one acre of land, its really not that big of a deal 2",
            "price": 1,
            "genre": Genres.RACING,
        },
    ]

    devs = {"Steve Dev Guy": steve_games, "IndieSpindie123": spindie_games}

    feedbacks = [
        {
            "game": spindie_games[0].get("name"),
            "feedback": """I really loovveed this game, getting to destroy something and it not 
                        being a big deal is a really big deal in todays gaming landscape haha""",
            "user": "Bill Big Guy",
            "rating": 10,
        },
        {
            "game": steve_games[1].get("name"),
            "feedback": """ I was ready to give up gaming before I came across to this game. 
                        It restored my self perception as I played with ease and satisfied 
                        my endless seek for approval and sucess. I will tell my therapist 
                        how helpful this was. It may replace my antidepressants. """,
            "user": "Petit Pois!",
            "rating": 3,
        },
        {
            "game": steve_games[1].get("name"),
            "feedback": """This game sucks!! Its just a rip off of Hollow Knight, the better game!""",
            "user": "Darren",
            "rating": 7,
        },
    ]

    for genre in list(Genres):
        genre = add_genre(genre)

    for dev, games in devs.items():
        d = add_dev(dev)
        for g in games:
            game = add_game(d, g["name"], g["price"], g["genre"])
            if g.get("description"):
                game.description = g["description"]
                game.save()

    for feedback in feedbacks:
        u = add_user(feedback["user"])
        f = add_feedback(feedback["feedback"], feedback["game"], u, feedback["rating"])

    for d in UserProfile.objects.all():
        if d.is_dev:
            print(f"{d} is a dev: {d.is_dev}")
            for g in Game.objects.filter(dev=d):
                print(f"\t{g}")
                for f in Feedback.objects.filter(game=g):
                    print(f"\t\t{f}")


def add_genre(genre):
    genre = Genre.objects.get_or_create(name=genre)[0]
    genre.save()
    return genre


def add_dev(dev):
    user = User.objects.get_or_create(username=dev)[0]
    user.save()
    d = UserProfile.objects.get_or_create(user=user, is_dev=True)[0]
    d.save()
    return d


def get_dev(dev):
    d = UserProfile.objects.get(user=User.objects.get(username=dev))
    return d


def add_game(dev, name, price, genre):
    d = get_dev(dev)
    g = Game.objects.get_or_create(name=name, dev=d)[0]
    g.price = price
    g.genre = Genre.objects.get(name=genre)
    g.save()
    return g


def get_game(game):
    g = Game.objects.get(name=game)
    return g


def add_user(username):
    user = User.objects.get_or_create(username=username)[0]
    user.save()
    profile = UserProfile.objects.get_or_create(user=user, is_dev=False)[0]
    profile.save()
    return profile


def add_feedback(feeback, game, userProfile, rating):
    g = get_game(game)
    f = Feedback.objects.get_or_create(
        text=feeback, game=g, userProfile=userProfile, rating=rating
    )[0]
    f.save()
    return f


if __name__ == "__main__":
    print("Starting Indie Population Script...")
    populate()
