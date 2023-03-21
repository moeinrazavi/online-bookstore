# Online Bookstore

This is a simple web application built with Django and MySQL, providing an interface for managing an online bookstore. Users can view, add, and search for customers, books, and orders.

## Prerequisites

- Python 3.8 or later
- Django 4.1 or later
- MySQL 8.0 or later

## Installation

1. Clone the repository or download the project files.

git clone https://github.com/moeinrazavi/online-bookstore.git
cd online-bookstore


2. Create a virtual environment and activate it.

python3 -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate


3. Install the required dependencies.

pip install -r requirements.txt


4. Update the `settings.py` file with your MySQL database connection details.

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'your_database_name',
    'USER': 'your_database_user',
    'PASSWORD': 'your_database_password',
    'HOST': 'localhost',
    'PORT': '3306',
    }
}


5. Apply the migrations to create the necessary tables in the MySQL database.


python manage.py migrate



## Running the Application

1. Start the Django development server.


python manage.py runserver



2. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

## Features

- List customers, books, and orders
- Add new customers, books, and orders
- Search for customers by name patterns
- Sort and filter books by price

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


