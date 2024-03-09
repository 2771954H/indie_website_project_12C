import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      'wad_indie_website_12c.settings')

import django
django.setup()
from indie.models import Genre,Game,Feedback,UserProfile
from django.contrib.auth.models import User
from enum import Enum

def populate():
    
    class Genres(Enum):
        FARMING_SIMULATOR = 1
        PLATFORMER =2
        ACTION_ADVENTURE = 3
        SURVIVAL_HORROR = 4
        RPG = 5
        FPS = 6
        RACING = 7
        FISHING_HORROR_SIMULATOR = 8
        HOLLOW_LIKE = 9
        
    steve_games = [
        {'name' : 'Jumper of Planet S',
         'price' : 30,
         'genre' : Genres.FARMING_SIMULATOR},
        
        {'name' : 'Empty Sir for Dummies',
         'price' : 15,
         'genre' : Genres.HOLLOW_LIKE},
        
        {'name' : 'Crush those Pistachio Shells (Rip-off Candy Crush)',
         'price': 150,
         'genre' : Genres.FISHING_HORROR_SIMULATOR}
    ]
    
    spindie_games = [
        {'name' : 'Destroyer of only one acre of land, its really not that big of a deal',
         'price' : 0.5,
         'genre': Genres.ACTION_ADVENTURE},
        
        {'name' : 'Destroyer of only one acre of land, its really not that big of a deal 2',
         'price' : 1,
         'genre' : Genres.RACING}
    ]
    
    devs = { 'Steve Dev Guy' : steve_games,
        'IndieSpindie123' : spindie_games
        }

    
    for genre in list(Genres):
        genre = add_genre(genre)
        
    for dev, games in devs.items():
        d = add_dev(dev)
        for g in games:
            add_game(d, g['name'], g['price'], g['genre'])
            
    for d in UserProfile.objects.all():
        if d.is_dev:
            for g in Game.objects.filter(dev=d):
                print(f"- {d}: {g}")
        

def add_genre(genre):
    genre = Genre.objects.get_or_create(name=genre)[0]
    genre.save()
    return genre

def add_dev(dev):
    user = User.objects.get_or_create(username = dev)[0]
    user.save()
    d = UserProfile.objects.get_or_create(user=user, is_dev = True)[0]
    d.save()
    return d

def get_dev(dev):
    d = UserProfile.objects.get(user= User.objects.get(username = dev))
    print(d)
    return d

def add_game(dev, name, price, genre):
    d = get_dev(dev)
    print(d)
    g = Game.objects.get_or_create(name = name, dev = d)[0]
    g.price=price
    g.genre = Genre.objects.get(name = genre)
    g.save()
    return g

if __name__== '__main__':
    print("Starting Indie Population Script...")
    populate()
    