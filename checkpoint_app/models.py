from django.db import models
from django.contrib.auth.models import User  


class Game(models.Model):
    game_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField()
    platform = models.CharField(max_length=100)

    userGame = models.ForeignKey('UserGame', on_delete=models.SET_NULL, null=True, blank=True)
    review = models.ForeignKey('Review', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.game_name

# 🎯 UserGame Model
class UserGame(models.Model):
    is_completed = models.BooleanField(default=False)
    playtime_hours = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    # null=True  → Allows the field to be NULL in the database (optional data)
    # blank=True → Allows the field to be left empty in forms (not required in user input)
    # Together, they make the field optional both in the database and in Django forms

    def __str__(self):
        return f'UserGame #{self.id}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} - {self.rating}'
