from django.contrib import admin
from indie.models import Genre, Game, Feedback, UserProfile


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "price_formatted",
        "likes",
        "views",
        "downloads",
        "genre",
        "dev",
        "featured",
        "upload_date",
    ]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["game", "userProfile", "rating", "text"]


admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(UserProfile)
