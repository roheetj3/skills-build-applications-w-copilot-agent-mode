# Test data for Octofit (Merington High School) fitness tracker app
# Based on the MonaFit tracker sample data

test_data = {
    "users": [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ],
    "teams": [
        {"name": "Blue Team", "members": ["thundergod", "metalgeek", "zerocool"]},
        {"name": "Gold Team", "members": ["crashoverride", "sleeptoken"]},
    ],
    "activities": [
        {"user": "thundergod", "activity_type": "Cycling", "duration": 60},
        {"user": "metalgeek", "activity_type": "Crossfit", "duration": 120},
        {"user": "zerocool", "activity_type": "Running", "duration": 90},
        {"user": "crashoverride", "activity_type": "Strength", "duration": 30},
        {"user": "sleeptoken", "activity_type": "Swimming", "duration": 75},
    ],
    "leaderboard": [
        {"user": "thundergod", "score": 100},
        {"user": "metalgeek", "score": 90},
        {"user": "zerocool", "score": 95},
        {"user": "crashoverride", "score": 85},
        {"user": "sleeptoken", "score": 80},
    ],
    "workouts": [
        {"name": "Cycling Training", "description": "Training for a road cycling event"},
        {"name": "Crossfit", "description": "Training for a crossfit competition"},
        {"name": "Running Training", "description": "Training for a marathon"},
        {"name": "Strength Training", "description": "Training for strength"},
        {"name": "Swimming Training", "description": "Training for a swimming competition"},
    ]
}
