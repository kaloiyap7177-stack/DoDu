"""
WSGI config for dudo_project project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments for PythonAnywhere.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project directory to Python path
path = '/home/yourusername/dudo_project'  # Change this to your actual path
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dudo_project.settings')

application = get_wsgi_application()