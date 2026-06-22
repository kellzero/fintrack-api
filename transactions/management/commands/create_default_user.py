from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Creates a default user for production'

    def handle(self, *args, **kwargs):
        username = os.environ.get('DEFAULT_USERNAME', 'admin')
        password = os.environ.get('DEFAULT_PASSWORD', 'admin123')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password)
            self.stdout.write(f'User {username} created successfully')
        else:
            self.stdout.write(f'User {username} already exists')