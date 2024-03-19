from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse

from indie.models import Game, User, UserProfile
from indie.forms import GameForm, UserForm, UserProfileForm


def index(request):
    context_dict = {}

    featured_games_list = Game.objects.filter(featured=True)[:4]
    popular_games_list = Game.objects.order_by("-downloads")[:4]
    new_games_list = Game.objects.order_by("-upload_date")[:4]
    top_games_list = Game.objects.order_by("-likes")[:4]

    context_dict["featured_games"] = featured_games_list
    context_dict["popular_games"] = popular_games_list
    context_dict["new_games"] = new_games_list
    context_dict["top_games"] = top_games_list

    return render(request, "indie/index.html", context=context_dict)


def search(request):
    query = request.GET.get("searchtext")
    context_dict = {}

    games_list = Game.objects.filter(name__contains=query)
    devs_list = User.objects.filter(username__contains=query, userprofile__is_dev=True)

    context_dict["games"] = games_list
    context_dict["devs"] = devs_list
    context_dict["query"] = query

    return render(request, "indie/search.html", context=context_dict)


def show_game(request, game_name_slug):
    context_dict = {}

    try:
        game = Game.objects.get(slug=game_name_slug)
        context_dict["game"] = game
    except Game.DoesNotExist:
        context_dict["game"] = None

    return render(request, "indie/game_page.html", context=context_dict)


def show_user(request, username):
    context_dict = {}

    try:
        user = UserProfile.objects.get(user__username=username)
        context_dict["user"] = user
    except UserProfile.DoesNotExist:
        context_dict["user"] = None

    context_dict["username"] = username

    return render(request, "indie/user_page.html", context=context_dict)


def register(request):
    registered = False
    context_dict = {}

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES["picture"]

            profile.save()

            registered = True
            context_dict["user"] = user
            context_dict["profile"] = profile
            login(request, user)

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict["user_form"] = user_form
    context_dict["profile_form"] = profile_form
    context_dict["registered"] = registered

    return render(request, "indie/register.html", context=context_dict)


def user_login(request):
    context_dict = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            try:
                profile = UserProfile.objects.get(user=user)
            except:
                # superusers you create via the command line won't have profiles asscociated with them
                # probably won't need this as users will create their accounts via the form
                profile = UserProfile.objects.create(user=user)
            if user.is_active:
                login(request, user)
                if profile.is_dev:
                    return redirect(reverse("indie:dev_home"))
                else:
                    return redirect(reverse("indie:index"))
            else:
                context_dict["error"] = "Your Indie account is disabled."
        else:
            context_dict["error"] = "Invalid login details."
    return render(request, "indie/login.html", context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("indie:index"))


# Dev pages
def dev_home(request):
    context_dict = {}

    return render(request, "indie/dev_home.html", context=context_dict)


def upload_game(request):
    context_dict = {}

    form = GameForm()

    if request.method == "POST":
        form = GameForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("indie/dev_home.html")

        else:
            print(form.errors)

    return render(
        request, "indie/upload_game.html", {"form": form}, context=context_dict
    )
