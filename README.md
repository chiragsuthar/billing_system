# Billing System

This is a billing system project built with Django.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/chiragsuthar/billing_system.git
   cd billing_system

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env

3. **Activate the Virtual Environment**:
 
    On Windows:
      ```bash
      .\env\Scripts\activate
      ```
    On macOS and Linux:
      ```bash
      source env/bin/activate

5. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

6. Run Migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

7. **Create a Superuser (for admin access)**:
    ```bash
    python manage.py createsuperuser

8. **How to Run**
Run the Development Server:
    ```bash
    python manage.py runserver
    
Access the Application:Open your web browser and go to http://127.0.0.1:8000/ to access the application.
Admin Panel:You can access the admin panel at http://127.0.0.1:8000/admin/. Log in with the superuser credentials created earlier.

**Additional Information**

Database:By default, the project uses SQLite as its database. You can change the database configuration in billing_system/settings.py if needed.

Environment Variables:If you have any environment variables, you can set them in a .env file in the project directory.

**Requirements**

Python 3.x
Django 3.x
Other dependencies specified in requirements.txt
