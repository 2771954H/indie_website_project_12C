from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Genre(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    MAX_INPUT_LENGTH = 9999

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique = True)
    is_dev = models.BooleanField(default=False)
    bio = models.CharField(max_length=MAX_INPUT_LENGTH, blank=True, null=True)
    paypal_address = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to="profile_images", blank=True, null=True)
    fav_genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, blank=True
    )
    

    def __str__(self):
        return self.user.username   


class Game(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=128, unique=True)
    price = models.FloatField(default=0)

    def price_formatted(self):
        return f"£{self.price:.2f}"

    price_formatted.short_description = "Price"

    likes = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(default=0, blank=True)
    downloads = models.IntegerField(default=0, blank=True)

    slug = models.SlugField(unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    dev = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null =True)
    
    #Have not tested this at all- no idea if it actually works
    def dev_check(self):
        dev = self._meta.get_fields()[7]
        if not dev._meta.get_fields()[1]:
            raise KeyError("Games creator must be a dev user")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    MAX_INPUT_LENGTH = 9999

    text = models.CharField(max_length=MAX_INPUT_LENGTH)
    rating = models.IntegerField()
    userProfile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null = True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.userProfile} wrote review for {self.game}. Gave rating of {self.rating}"


