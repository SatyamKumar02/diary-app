diary-app/
│
├── app/
│   ├── __init__.py         # Initializes Flask app, DB, LoginManager
│   ├── routes.py           # Contains all Flask routes
│   ├── models.py           # User and Entry models
│   ├── forms.py            # WTForms for login, signup, diary
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── dashboard.html
│   │   └── entry_form.html
│   |   ├── calendar.html
│   |   └── profile.html
│   └── static/
│       ├── style.css
|       └── default-avatar.png
│
├── .env                    # For secrets (e.g., Mongo URI, Flask secret key)
├── config.py               # Config class for Flask app
├── run.py                  # Entry point to run the app
├── requirements.txt        # List of dependencies
└── README.md               # Project overview


in commnd prompt - run cmd -> mongo

PS F:\MY_LIFE_MY_VIEWS\my projects\personal_diary_app\diary-app> venv\Scripts\activate
python run.py
====================================
signed up - satyam, satyamksingh02@gmail.com, 123456



====================================

🚀 Core Technologies
Package	Version	Purpose
Flask	3.1.0	The main web framework you're using. Lightweight, flexible, perfect for APIs or full-stack apps.
Jinja2	3.1.6	The templating engine Flask uses to render HTML with Python logic.
Werkzeug	3.1.3	Flask’s core WSGI utility library – handles routing, requests, responses.
itsdangerous	2.2.0	Used by Flask to securely sign data (e.g., cookies, tokens).
click	8.1.8	Used for creating command-line tools (Flask’s CLI commands use it).
MarkupSafe	3.0.2	Escapes characters in HTML to prevent injection attacks. Used in templates.

👥 User Authentication & Forms
Package	Version	Purpose
Flask-Login	0.6.3	Manages user sessions (log in/out, remember user).
Flask-WTF	1.2.2	Integrates Flask with WTForms for form validation & CSRF protection.
WTForms	3.2.1	A library for creating and validating web forms.
email_validator	2.2.0	Validates email fields in WTForms (used in Email() validator).

🗃️ Database Connectivity
Package	Version	Purpose
pymongo	4.11.3	Official MongoDB driver for Python – used to interact with your MongoDB database.
dnspython	2.7.0	Handles DNS resolution, especially helpful when using MongoDB connection strings (like mongodb+srv://...).

⚙️ Utility Libraries
Package	Version	Purpose
python-dotenv	1.1.0	Loads environment variables from a .env file. Keeps secrets/configs out of code.
colorama	0.4.6	Makes colored terminal output work on Windows (often used in CLI tools).
blinker	1.9.0	A signaling library. Flask uses this for things like event handling (signals, e.g., user_logged_in).
idna	3.10	Handles international domain names (e.g., for email or URLs). Required by dnspython.

✅ Summary by Technology Type
Web Framework: Flask, Werkzeug, Jinja2, itsdangerous
Authentication & Forms: Flask-Login, Flask-WTF, WTForms, email-validator
Database (MongoDB): pymongo, dnspython
Environment & Config: python-dotenv
Utility & CLI: click, colorama, blinker, idna

🧱 So, Your Tech Stack Is:
Backend: Flask (Python)
Templating: Jinja2
Auth & Forms: Flask-Login + Flask-WTF + WTForms
Database: MongoDB (via pymongo)
Environment Handling: .env with python-dotenv