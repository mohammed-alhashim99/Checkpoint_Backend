from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    game_id = models.IntegerField(unique=True)
    game_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.FloatField()
    platform = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.game_name

class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    playtime_hours = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'game')  

    def __str__(self):
        status = "✅" if self.is_completed else "⏳"
        return f'{self.user.username} - {self.game.game_name} {status}'
    def __str__(self):
        user_str = self.user.username if self.user else "Anonymous"
        game_str = self.game.game_name if self.game else "No Game"
        return f'{user_str} - {game_str}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.FloatField()
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review: {self.game.game_name} by {self.user.username}'
