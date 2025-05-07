from django.test import TestCase
from django.contrib.auth.models import User
from checkpoint_app.models import Game, UserGame, Review
from datetime import date, datetime

class GameAppModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='gamer', password='1234')
        self.game = Game.objects.create(
            game_id=100,
            game_name='Elden Ring',
            release_date=date(2022, 2, 25),
            rating=4.9,
            platform='PC, PS5',
            image_url='http://example.com/eldenring.jpg'
        )
        self.user_game = UserGame.objects.create(
            user=self.user,
            game=self.game,
            is_completed=True,
            playtime_hours=120,
            completed_at=datetime(2023, 1, 1)
        )
        self.review = Review.objects.create(
            user=self.user,
            game=self.game,
            rating=5.0,
            description='Masterpiece!'
        )

    def test_game_created(self):
        self.assertEqual(self.game.game_name, 'Elden Ring')
        self.assertEqual(str(self.game), 'Elden Ring')

    def test_usergame_created(self):
        self.assertEqual(self.user_game.playtime_hours, 120)
        self.assertTrue(self.user_game.is_completed)
        self.assertEqual(str(self.user_game), 'gamer - Elden Ring')

    def test_review_created(self):
        self.assertEqual(self.review.rating, 5.0)
        self.assertEqual(str(self.review), 'Review: Elden Ring by gamer')

    def test_user_relationship(self):
        self.assertEqual(self.user_game.user, self.user)
        self.assertEqual(self.review.user, self.user)

    def test_game_relationship(self):
        self.assertEqual(self.user_game.game, self.game)
        self.assertEqual(self.review.game, self.game)

    def test_cascade_delete_user(self):
        self.user.delete()
        self.assertEqual(UserGame.objects.count(), 0)
        self.assertEqual(Review.objects.count(), 0)

    def test_cascade_delete_game(self):
        self.game.delete()
        self.assertEqual(UserGame.objects.count(), 0)
        self.assertEqual(Review.objects.count(), 0)

    def test_unique_together_constraint(self):
        with self.assertRaises(Exception):
            UserGame.objects.create(
                user=self.user,
                game=self.game,
                is_completed=False
            )
