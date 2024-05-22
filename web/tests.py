import os, sys, django, requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "highlight.settings")
from django.conf import settings
sys.path.append( settings.BASE_DIR )
django.setup()


from django.test import TestCase
from web.models import User
# Create your tests here.

def list_all_users():
    
    all_users = User.objects.all()
    for user in all_users:
        print(f"Name: {user.name}, Email: {user.email}, Place: {user.place}")

list_all_users()