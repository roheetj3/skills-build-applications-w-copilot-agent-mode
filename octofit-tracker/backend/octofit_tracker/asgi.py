"""
ASGI config for octofit_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
>>>>>>> 9d8d899 (Populate octofit_db with test data, add test_octofit_data.py, and update management command)
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
>>>>>>> 9d8d899 (Populate octofit_db with test data, add test_octofit_data.py, and update management command)

application = get_asgi_application()
