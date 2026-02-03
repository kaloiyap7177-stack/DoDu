# PythonAnywhere Deployment Checklist

## Before Deploying

- [ ] Ensure all changes are committed and pushed to your repository
- [ ] Test the application locally to make sure everything works
- [ ] Update the `requirements.txt` file if you've added new packages

## On PythonAnywhere Dashboard

### 1. Create Account & Setup
- [ ] Create account at https://www.pythonanywhere.com/
- [ ] Verify your email address
- [ ] Log in to your dashboard

### 2. Upload Project Files
- [ ] Option A: Upload files manually via Files tab
- [ ] Option B: Clone from GitHub repository
- [ ] Option C: Upload a ZIP file and extract

### 3. Create Virtual Environment
- [ ] Open Bash console
- [ ] Create virtual environment:
  ```bash
  mkvirtualenv --python=python3.13 dudo_env
  ```
- [ ] Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Update Settings
- [ ] Edit `dudo_project/settings.py`
- [ ] Update `ALLOWED_HOSTS` with your domain:
  ```python
  ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
  ```
- [ ] Update database path if using SQLite (full absolute path):
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': '/home/yourusername/dudo_project/db.sqlite3',  # Full path required
      }
  }
  ```

### 5. Run Migrations
- [ ] Run database migrations:
  ```bash
  python manage.py migrate
  ```
- [ ] Create superuser (optional):
  ```bash
  python manage.py createsuperuser
  ```

### 6. Configure Web App
- [ ] Go to Web tab
- [ ] Click "Add a new web app"
- [ ] Choose "Manual configuration" (not Django!)
- [ ] Select Python 3.13
- [ ] Set the path to your project directory
- [ ] In the "Code" section, update the path to your project
- [ ] In the "Virtualenv" section, set path to your virtual environment

### 7. Configure WSGI File
- [ ] Edit the WSGI file in `/var/www/`
- [ ] Replace contents with:
  ```python
  import os
  import sys
  
  # Add your project directory to Python path
  path = '/home/yourusername/dudo_project'  # Change to your actual path
  if path not in sys.path:
      sys.path.insert(0, path)
  
  os.environ['DJANGO_SETTINGS_MODULE'] = 'dudo_project.settings'
  
  from django.core.wsgi import get_wsgi_application
  application = get_wsgi_application()
  ```

### 8. Collect Static Files
- [ ] Run collectstatic command:
  ```bash
  python manage.py collectstatic --noinput
  ```
- [ ] Or configure static files in Web tab:
  - URL: `/static/`
  - Directory: `/home/yourusername/dudo_project/staticfiles/`

### 9. Reload Web App
- [ ] Click "Reload" button on the Web tab
- [ ] Check for any error messages

## Troubleshooting

### Common Issues:
- [ ] Check error logs in `/var/log/pythonanywhere.com-yourdomain_com.error.log`
- [ ] Ensure all file permissions are correct
- [ ] Verify that the virtual environment is activated and has all dependencies
- [ ] Make sure paths in settings.py are absolute paths

### Testing:
- [ ] Visit your site at `https://yourusername.pythonanywhere.com`
- [ ] Test all functionality
- [ ] Verify static files are loading properly

## Post-Deployment

- [ ] Update the admin password
- [ ] Add your own content and customize as needed
- [ ] Monitor the application for any issues
- [ ] Set up automated backups if needed