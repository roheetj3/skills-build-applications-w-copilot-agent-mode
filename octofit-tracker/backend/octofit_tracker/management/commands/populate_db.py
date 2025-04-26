from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

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
