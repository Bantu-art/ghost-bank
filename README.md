# ghost-bank

A modern full-stack banking application built with Django (backend) and React (frontend), using Vite and Tailwind CSS for rapid development and a beautiful UI.

## Project Structure

```
ghostbenkiweb/
  backend/         # Django backend (API, admin, business logic)
    accounts/      # Django app for user accounts
    ghostbenki/    # Django project settings and core
    static/        # Static files for backend
  frontend/        # React frontend (Vite, Tailwind)
    src/           # React source code
    static/        # Frontend static assets
staticfiles/       # Collected static files (Django)
templates/         # Django HTML templates
```

## Features

- User authentication and account management (Django)
- Modern, responsive UI (React + Tailwind CSS)
- API-driven architecture (Django REST Framework ready)
- Hot-reloading development environment (Vite)
- Easy static file management

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn

### Backend Setup (Django)

1. Install dependencies:
   ```bash
   cd ghostbenkiweb/backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Start the backend server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup (React + Vite)

1. Install dependencies:
   ```bash
   cd ghostbenkiweb/frontend
   npm install
   ```

2. Start the frontend dev server:
   ```bash
   npm run dev
   ```

### Static Files

- Collect static files for production:
  ```bash
  cd ghostbenkiweb/backend
  python manage.py collectstatic
  ```

## Development

- Backend: http://localhost:8000/
- Frontend: http://localhost:5173/

## Deployment

- Configure environment variables and production settings in `ghostbenkiweb/backend/ghostbenki/settings.py`.
- Use a production-ready server (e.g., Gunicorn, Nginx) for deployment.

## License

This project is licensed under the MIT License.