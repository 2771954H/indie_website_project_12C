from django import forms
from django.contrib.auth.models import User
from indie.models import Genre, Game, Feedback, UserProfile
from datetime import date


class GenreForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Genre.NAME_MAX_LENGTH,
        help_text="Please enter the genre name.",
        required=True,
    )
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Genre
        fields = ("name",)


class GameForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Game.NAME_MAX_LENGTH,
        help_text="Please enter the game name.",
        required=True,
    )
    price = forms.FloatField(initial=0, required=True, help_text="Please enter the price you want your game to be")

    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    downloads = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    upload_date = forms.DateField(widget=forms.HiddenInput(), initial=date.today())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    genre = forms.ModelChoiceField(queryset= Genre.objects, required=False, help_text="Please enter the genre your game is")
    image = forms.ImageField(initial="static/images/no_image.jpg", required=False, help_text="Please upload the image for your game")

    class Meta:
        model = Game
        fields = ("name", "price", "genre",)
'''
class FeedbackForm(forms.ModelForm):
    text = forms.CharField(
        max_length=Feedback.MAX_INPUT_LENGTH,
        help_text="Please enter your feedback.",
        required=True,
    )
    rating = forms.IntegerField(
        help_text="What would you rate the game out of 10?", required=True
    )
    #InineForeginKey Field does not exist
    user = forms.InlineForeignKeyField(required=True)
    game = forms.InlineForeignKeyField(required=True)

    class Meta:
        model = Feedback
        fields = ("text", "rating", "user", "game")
'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )


class UserProfileForm(forms.ModelForm):
    is_dev = forms.BooleanField(required=False, help_text="Are you wanting a Developer profile? (Tick if yes)")
    class Meta:
        model = UserProfile
        fields = (
            "paypal_address",
            "picture",
            "is_dev",
        )
