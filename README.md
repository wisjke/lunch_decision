# Lunch Decision Making App

A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.

# Tech Stack

This project is built using the following technologies:
Django, Django Rest Framework (DRF), JWT, PostgreSQL, PyTest

# Installation
Clone the repository:
Copy ```git clone https://github.com/wisjke/lunch_decision```
```cd [your-project-directory]```

Create a virtual environment and activate it:
Install the required dependencies:
Copypip ```install -r requirements.txt```

Set up the PostgreSQL database and update the database configuration in settings.py.

Run migrations:

Copy ```python manage.py migrate```

Running the Application
To run the application, use the following command:
Copy ```python manage.py runserver```
The application will start and be available at ```http://localhost:8000.```

# API Endpoints

```api/create_restaurant/```: Create a new restaurant

```api/menus/```: Manage restaurant menus

```api/create_employee/```: Register a new employee

```api/votes/```: Manage and submit votes

```api/token/```: Obtain JWT token

```api/token/refresh/```: Refresh JWT token
