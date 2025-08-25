# KYC Demo Project

This is a lightweight KYC (Know Your Customer) solution built with Django, designed for local development. The project demonstrates a simple flow for user verification and document submission.

## Features

- User registration and login
- Document upload for Aadhaar and PAN
- Face verification through selfie capture
- Consent receipt generation
- Admin interface for managing KYC submissions

## Project Structure

```
kyc_demo/
├── kyc_demo/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── kyc/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── kyc/
│       ├── base.html
│       ├── kyc_form.html
│       └── kyc_success.html
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd kyc_demo
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## User Flows

- **Document Upload:** Users can upload their Aadhaar or PAN documents.
- **Face Capture:** Users can capture their selfie for verification.
- **Consent Receipt:** After successful KYC, users receive a consent receipt.

## License

This project is licensed under the MIT License. See the LICENSE file for details.