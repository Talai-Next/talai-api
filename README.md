# Talai mockup RESTful API

This project is a Django-based providing a RESTful API using the Django REST Framework (DRF) for show Talai data.

---

## Features

- RESTful API with Django REST Framework
- Route data integration via Pandas and CSV files (line_1, line_3, line_5, and SP)
- SQLite database
- Modular structure for apps

---

## Requirements

Make sure you have the following installed:
- Python 3.8+
- pip / pipenv / poetry
- Git

---

## Installation & Setup

### Clone the Repository

```bash
https://github.com/Talai-Next/backend.git](https://github.com/Talai-Next/talai-api.git
```

### Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root (if used), or update `settings.py` for:

```env
DATABASE_URL=your-database-url
DJANGO_SECRET_KEY=your-secret-key
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


### Run Development Server

```bash
python manage.py runserver 8080
```

Your API will be available at: [http://localhost:8080/](http://localhost:8080/)



## Project Structure (Example)

```
├── tracking/
│   ├── migrations/
│   ├── serializers/
│   ├── tests/
│   ├── views/
│   └── urls.py
├── talaiapi/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
├── .gitignore
└── .env
```


---

## Useful Commands

```bash
python manage.py runserver          # Start dev server
python manage.py makemigrations    # Create migrations
python manage.py migrate           # Apply migrations
python manage.py createsuperuser   # Create admin user
```

---

## License

This project is licensed under the MIT License.
