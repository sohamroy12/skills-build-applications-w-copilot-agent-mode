from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team.name)
        self.assertEqual(user.name, 'Test User')

    def test_team_create(self):
        team = Team.objects.create(name='Another Team', description='desc')
        self.assertEqual(team.name, 'Another Team')

    def test_activity_create(self):
        Activity.objects.create(user='Test User', activity_type='Run', duration=10, date='2025-11-24')
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard_create(self):
        Leaderboard.objects.create(user='Test User', score=42)
        self.assertEqual(Leaderboard.objects.count(), 1)

    def test_workout_create(self):
        Workout.objects.create(name='Pushup', description='desc', difficulty='Easy')
        self.assertEqual(Workout.objects.count(), 1)
