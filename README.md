# Uz-Koram Xarid Xizmati

Django foundation for the Uz-Koram procurement service automation project.

## Stack

- Python and Django
- Server-rendered Django templates with a shared `base.html`
- SQLite for local development

Docker and MySQL are intentionally not configured for this implementation.

## Local Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Tests

```powershell
python manage.py test
python manage.py check
```
