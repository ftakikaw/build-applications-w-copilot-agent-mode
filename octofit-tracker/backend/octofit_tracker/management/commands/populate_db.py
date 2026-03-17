from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel),
            User.objects.create_user(email='captain@marvel.com', username='captain', team=marvel),
            User.objects.create_user(email='batman@dc.com', username='batman', team=dc),
            User.objects.create_user(email='superman@dc.com', username='superman', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30)
        Activity.objects.create(user=users[1], type='cycle', duration=45)
        Activity.objects.create(user=users[2], type='swim', duration=60)
        Activity.objects.create(user=users[3], type='walk', duration=20)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for superheroes')
        Workout.objects.create(name='Strength Training', description='Strength for superheroes')

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=80)
        Leaderboard.objects.create(user=users[3], points=70)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
