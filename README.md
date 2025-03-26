✅ User-friendly contact form
✅ Data storage using Django models
✅ Basic page navigation
✅ Prevents form resubmission on page refresh

Technologies Used
Python (Django Framework)
HTML & CSS (For frontend templates)
SQLite (Default Django database)
Bootstrap (Optional for styling)

Installation
. git clone https://github.com/your-username/simple-django-app.git
  cd simple-django-app
. python -m venv venv  
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
. pip install -r requirements.txt
. python manage.py migrate
.  python manage.py runserver
. http://127.0.0.1:8000/

How It Works
. The user fills out a contact form.
. Upon submission, the data is validated and saved in the database.
. A success message is displayed, and the user is redirected to prevent duplicate submissions on refresh.

Future Enhancements
🔹 Add user authentication
🔹 Store form submissions in an admin panel
