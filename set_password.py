import os
import django
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dudo_project.settings')
django.setup()

from django.contrib.auth.models import User

# Set password for admin user
try:
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.save()
    print("Password set successfully for admin user")
except User.DoesNotExist:
    print("Admin user not found")