from django.core.management.base import BaseCommand
<<<<<<< HEAD
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId
=======
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId
import json
import os
>>>>>>> 9d8d899 (Populate octofit_db with test data, add test_octofit_data.py, and update management command)

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
<<<<<<< HEAD
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

=======
        # Load test data from test_octofit_data.py
        from octofit_tracker.test_octofit_data import test_data

        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
>>>>>>> 9d8d899 (Populate octofit_db with test data, add test_octofit_data.py, and update management command)
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

<<<<<<< HEAD
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
        ]
        db.users.insert_many(users)

        teams = [
            {"_id": ObjectId(), "name": "Avengers", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Hackers", "members": [users[2]["_id"], users[3]["_id"]]},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "run", "duration": 30},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "walk", "duration": 45},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "cycle", "duration": 60},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "swim", "duration": 25},
        ]
        db.activity.insert_many(activities)

        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 80},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 70},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
            {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps"},
            {"_id": ObjectId(), "name": "Running", "description": "Run for 15 minutes"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
=======
        # Insert users
        user_objs = {}
        for user in test_data['users']:
            user_doc = user.copy()
            user_doc['_id'] = ObjectId()
            db.users.insert_one(user_doc)
            user_objs[user['username']] = user_doc['_id']

        # Insert teams
        for team in test_data['teams']:
            team_doc = {
                '_id': ObjectId(),
                'name': team['name'],
                'members': [user_objs[uname] for uname in team['members']]
            }
            db.teams.insert_one(team_doc)

        # Insert activities
        for activity in test_data['activities']:
            activity_doc = {
                '_id': ObjectId(),
                'user': user_objs[activity['user']],
                'activity_type': activity['activity_type'],
                'duration': activity['duration']  # store as minutes
            }
            db.activity.insert_one(activity_doc)

        # Insert leaderboard
        for entry in test_data['leaderboard']:
            leaderboard_doc = {
                '_id': ObjectId(),
                'user': user_objs[entry['user']],
                'score': entry['score']
            }
            db.leaderboard.insert_one(leaderboard_doc)

        # Insert workouts
        for workout in test_data['workouts']:
            workout_doc = {
                '_id': ObjectId(),
                'name': workout['name'],
                'description': workout['description']
            }
            db.workouts.insert_one(workout_doc)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
>>>>>>> 9d8d899 (Populate octofit_db with test data, add test_octofit_data.py, and update management command)
