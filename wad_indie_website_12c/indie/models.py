from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Game(models.Model):
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    text = models.CharField(max_length=9999)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_dev = models.BooleanField(default=False)
    bio = models.CharField(max_length=9999, blank=True, null=True)
    paypal_address = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to="profile_images", blank=True, null=True)
    fav_genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.user.username
