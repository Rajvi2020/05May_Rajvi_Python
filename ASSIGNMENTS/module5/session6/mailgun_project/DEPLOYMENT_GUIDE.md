# 🚀 PythonAnywhere Deployment & Postman Testing Guide

This guide details how to deploy your Django REST Framework API to **PythonAnywhere** and test all 4 endpoints live using **Postman**.

---

## 🔒 Privacy & Environment Variables Setup

All API keys are securely decoupled from the codebase using `python-dotenv`.
Your real secret keys MUST be placed inside the `.env` file on PythonAnywhere. `.env` is listed in `.gitignore` so your keys will never be exposed in public repositories.

### Required Keys in `.env`:
```env
SECRET_KEY=your_django_secret_key_here
DEBUG=False
ALLOWED_HOSTS=.pythonanywhere.com,localhost,127.0.0.1

# Task 1: Mailgun Keys
MAILGUN_API_KEY=key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MAILGUN_DOMAIN=sandboxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org
MAILGUN_SENDER=Mailgun Welcome <mailgun@sandboxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org>

# Task 2: Twilio Keys
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+1xxxxxxxxxx

# Stripe Configuration (Task 3)
STRIPE_SECRET_KEY=

# Google OAuth Configuration (Task 4)
GOOGLE_CLIENT_ID=xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com
```

---

## 🛠️ Step-by-Step PythonAnywhere Deployment

1. **Log in to PythonAnywhere**:
   - Go to [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/) and open a **Bash Console**.

2. **Clone / Upload Project**:
   ```bash
   git clone <your-repo-url> mailgun_project
   cd mailgun_project
   ```
   *(Or create a zip file of this directory, upload it to PythonAnywhere via Files tab, and unzip it)*.

3. **Set Up Virtual Environment & Install Dependencies**:
   ```bash
   mkvirtualenv --python=python3.12 myenv
   pip install -r requirements.txt
   ```

4. **Create `.env` File on PythonAnywhere**:
   ```bash
   nano .env
   ```
   Paste your environment keys into `.env` and press `Ctrl+O` then `Enter` to save, `Ctrl+X` to exit.

5. **Run Migrations & Collect Static Files**:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

6. **Configure Web App**:
   - Go to the **Web** tab in PythonAnywhere dashboard.
   - Click **Add a new web app** -> Select **Manual configuration** -> Select **Python 3.12**.
   - Under **Virtualenv**: Set path to `/home/<your-username>/.virtualenvs/myenv`.
   - Under **Code**:
     - Source code path: `/home/<your-username>/mailgun_project`
     - Working directory: `/home/<your-username>/mailgun_project`
   - Edit the **WSGI configuration file** (click the WSGI file link):
     Replace everything with the contents of `pythonanywhere_wsgi.py` (remember to replace `YOUR_PYTHONANYWHERE_USERNAME` with your actual username).
   - Click **Reload `<your-username>.pythonanywhere.com`**.

---

## 📮 Postman Testing Guide & Endpoint Collection

Your live API base URL will be:
`https://<your-username>.pythonanywhere.com`

### 1. Welcome Email via Mailgun (`POST /api/send-email/`)
- **Method**: `POST`
- **URL**: `https://<your-username>.pythonanywhere.com/api/send-email/`
- **Headers**: `Content-Type: application/json`
- **Body** (raw JSON):
  ```json
  {
    "email": "user@example.com",
    "subject": "Welcome to Our App!",
    "message": "Thank you for signing up!"
  }
  ```
- **Constraint**: *Take a screenshot of Postman showing this 200 OK HTTP response for assignment submission!*

---

### 2. SMS Dispatch via Twilio (`POST /api/send-sms/`)
- **Method**: `POST`
- **URL**: `https://<your-username>.pythonanywhere.com/api/send-sms/`
- **Headers**: `Content-Type: application/json`
- **Body** (raw JSON):
  ```json
  {
    "phone_number": "+1234567890",
    "message": "Hello! Your verification code is 482910."
  }
  ```

---

### 3. Payment Simulation via Stripe (`POST /api/pay/`)
- **Method**: `POST`
- **URL**: `https://<your-username>.pythonanywhere.com/api/pay/`
- **Headers**: `Content-Type: application/json`
- **Body** (raw JSON):
  ```json
  {
    "amount": 2500,
    "currency": "usd",
    "description": "Pro Subscription Upgrade"
  }
  ```
- **Sample Response**:
  ```json
  {
    "status": "succeeded",
    "message": "Stripe payment intent created successfully",
    "transaction_id": "pi_3M...",
    "amount": 2500,
    "currency": "USD"
  }
  ```

---

### 4. Google Login & JWT Authentication (`POST /api/google-login/`)
- **Method**: `POST`
- **URL**: `https://<your-username>.pythonanywhere.com/api/google-login/`
- **Headers**: `Content-Type: application/json`
- **Body** (raw JSON):
  ```json
  {
    "email": "john.doe@gmail.com",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```
- **Response**: Returns user object and JWT `access` & `refresh` tokens for authentication.
