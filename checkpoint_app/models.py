from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    game_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField()
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.game_name


class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    playtime_hours = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    # null=True  → Allows the field to be NULL in the database (optional data)
    # blank=True → Allows the field to be left empty in forms (not required in user input)
    # Together, they make the field optional both in the database and in Django forms

    def __str__(self):
        return f"{self.user.username} - {self.game.game_name}"


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.game_name} Review"
