from django.shortcuts import render, redirect
from django.http import HttpResponse

from indie.models import Game
from indie.forms import GameForm, UserForm, UserProfileForm


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

def register(request):
    registered = False
    context_dict = {'pagename': 'Register'}
    
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user=user
            
            profile.save()
            
            registered = True
            context_dict['user'] = user
            context_dict['profile'] = profile
            
    
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    context_dict['pagename'] = 'Register'
    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered
    
    return render(request, 'indie/register.html',
                  context=context_dict
                  )
        


def logout(request):
    return index(request)


# Dev pages
def dev_home(request):
    context_dict = {}
    context_dict["pagename"] = "Dev Home"

    return render(request, "indie/dev_home.html", context=context_dict)


def upload_game(request):
    context_dict = {}
    context_dict["pagename"] = 'Upload Game'
    
    form = GameForm()
    
    if request.method == 'POST':
        form = GameForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)            
            return redirect("indie/dev_home.html")
        
        else:
            print(form.errors)
    
    return render(request, "indie/upload_game.html", {'form' : form}, context=context_dict)
