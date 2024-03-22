from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from indie.models import Game, UserProfile

class TestViews(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='12345')
        self.test_user_profile = UserProfile.objects.create(user=self.test_user)

        self.test_game = Game.objects.create(name='Test Game', dev=self.test_user_profile)

    def test_index_view(self):
        response = self.client.get(reverse('indie:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['featured_games'], ['<Game: Test Game>'])

    def test_show_game_view(self):
        response = self.client.get(reverse('indie:show_game', args=[self.test_game.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['game'], self.test_game)

    def test_user_login_view(self):
        response = self.client.post(reverse('indie:user_login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

        self.test_user_profile.is_dev = True
        self.test_user_profile.save()
        response = self.client.post(reverse('indie:user_login'), {'username': 'testuser', 'password': '12345'})
        self.assertRedirects(response, reverse('indie:dev_home'))