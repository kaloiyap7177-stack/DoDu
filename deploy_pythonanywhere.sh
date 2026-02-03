#!/bin/bash
# Deployment script for PythonAnywhere

echo "Setting up DuDo project on PythonAnywhere..."

# Install required packages
pip3.13 install -r requirements.txt

# Run database migrations
python3.13 manage.py migrate

# Create superuser if not exists
echo "from django.contrib.auth.models import User; import os; username='admin'; password='admin123'; email='admin@example.com'; if not User.objects.filter(username=username).exists(): User.objects.create_superuser(username, email, password); print('Superuser created successfully')" | python3.13 manage.py shell

# Collect static files
python3.13 manage.py collectstatic --noinput

echo "Setup complete!"
echo "Remember to:"
echo "1. Update ALLOWED_HOSTS in settings.py with your PythonAnywhere domain"
echo "2. Update DATABASE path in settings.py if using SQLite"
echo "3. Reload your web app from the PythonAnywhere dashboard"