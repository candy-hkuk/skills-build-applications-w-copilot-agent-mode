from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users (OctoFit test data)
        user1 = User.objects.create(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword')
        user2 = User.objects.create(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword')
        user3 = User.objects.create(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword')
        user4 = User.objects.create(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword')
        user5 = User.objects.create(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword')

        # Create teams
        team1 = Team.objects.create(name='Blue Team')
        team2 = Team.objects.create(name='Gold Team')
        team1.members.set([user1, user2, user3])
        team2.members.set([user4, user5])
        team1.save()
        team2.save()

        # Create activities
        try:
            print('Creating activity 1')
            Activity.objects.create(user=user1, activity_type='Cycling', duration=timedelta(hours=1))
            print('Creating activity 2')
            Activity.objects.create(user=user2, activity_type='Crossfit', duration=timedelta(hours=2))
            print('Creating activity 3')
            Activity.objects.create(user=user3, activity_type='Running', duration=timedelta(hours=1, minutes=30))
            print('Creating activity 4')
            Activity.objects.create(user=user4, activity_type='Strength', duration=timedelta(minutes=30))
            print('Creating activity 5')
            Activity.objects.create(user=user5, activity_type='Swimming', duration=timedelta(hours=1, minutes=15))
            self.stdout.write(self.style.SUCCESS('Activities created'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating activities: {e}'))

        # Create leaderboard
        try:
            Leaderboard.objects.create(user=user1, score=100)
            Leaderboard.objects.create(user=user2, score=90)
            Leaderboard.objects.create(user=user3, score=95)
            Leaderboard.objects.create(user=user4, score=85)
            Leaderboard.objects.create(user=user5, score=80)
            self.stdout.write(self.style.SUCCESS('Leaderboard created'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating leaderboard: {e}'))

        # Create workouts
        try:
            Workout.objects.create(name='Cycling Training', description='Training for a road cycling event')
            Workout.objects.create(name='Crossfit', description='Training for a crossfit competition')
            Workout.objects.create(name='Running Training', description='Training for a marathon')
            Workout.objects.create(name='Strength Training', description='Training for strength')
            Workout.objects.create(name='Swimming Training', description='Training for a swimming competition')
            self.stdout.write(self.style.SUCCESS('Workouts created'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating workouts: {e}'))

        self.stdout.write(self.style.SUCCESS('Test data populated successfully for OctoFit.'))
