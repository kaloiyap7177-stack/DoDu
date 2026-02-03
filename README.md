<<<<<<< HEAD
# DuDo - Task Management Website

A simple Django-based task management application with user authentication, task categorization, and MySQL database support.

## Features

- User authentication (login/logout)
- Task creation, editing, and deletion
- Task categorization with custom colors
- Task filtering by category and completion status
- Responsive Bootstrap-based UI
- MySQL database support

## Setup Instructions

### 1. Virtual Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup

#### Option A: Using SQLite (Default - for quick testing)

The application is configured to use SQLite by default, which requires no additional setup.

#### Option B: Using MySQL

1. Install MySQL Server on your system
2. Create a database:
   ```sql
   CREATE DATABASE dudo_db;
   ```

3. Update `dudo_project/settings.py`:
   - Open the file and find the `DATABASES` configuration
   - Comment out the SQLite configuration (the first DATABASES block)
   - Uncomment the MySQL configuration (the second DATABASES block)
   - Update the credentials as needed

4. Install MySQL client (if not already installed):
   ```bash
   pip install mysqlclient
   ```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
# Follow prompts to create admin user
```

Or use the provided script:
```bash
python set_password.py
```
(Default admin user: username=`admin`, password=`admin123`)

### 5. Start Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Usage

1. **Login**: Navigate to the admin login page or use the top navigation
2. **Create Categories**: Go to "Categories" → "New Category" to create task categories
3. **Create Tasks**: Go to "My Tasks" → "New Task" to create tasks
4. **Manage Tasks**: View, edit, or delete tasks from the task list
5. **Filter Tasks**: Use the sidebar filters to view tasks by category or completion status

## Project Structure

```
DuDo/
├── dudo_project/          # Django project settings
├── dudo_app/              # Main application
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   └── urls.py            # URL routing
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── set_password.py        # Utility script
```

## Models

- **Task**: Represents a task with title, description, completion status
- **Category**: Represents task categories with custom colors
- **TaskCategory**: Many-to-many relationship between tasks and categories

## Technologies Used

- **Django 6.0.1**: Web framework
- **MySQL/SQLite**: Database
- **Bootstrap 5.3.0**: Frontend framework
- **Font Awesome 6.0.0**: Icons

## Default Credentials

- **Username**: admin
- **Password**: admin123

## Notes

- The application uses Django's built-in authentication system
- All tasks and categories are user-specific
- The UI is fully responsive and works on mobile devices
- Template syntax errors in the editor are normal - they're Django template syntax, not actual errors

## Troubleshooting

1. **MySQL Connection Error**: Ensure MySQL server is running and credentials are correct
2. **Migration Issues**: Delete `db.sqlite3` and `dudo_app/migrations/` then re-run migrations
3. **Static Files**: Run `python manage.py collectstatic` for production deployment
=======
# DoDu
my first DoDu website
>>>>>>> 748e38f2f3950538aec1e06e82cee7d7ea253bb0
