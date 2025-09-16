# PredictiveInsights

## Overview

This is a Django-based web application that predicts the progress stage of candidates using a pre-trained machine learning model. Users can input candidate details through a form, and the system returns a predicted stage based on the model.

---

## Features

* Input candidate information via a web form.
* Predict the candidate’s stage using a pre-trained ML model.
* Simple, user-friendly interface.

---

## Tech Stack

* **Backend:** Django 5.0, Python 3.12
* **Frontend:** HTML, CSS (minimal styling)
* **Machine Learning:** Scikit-learn, Joblib
* **Database:** SQLite (development), MySQL (optional for production)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd CandidateProgress
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   # or
   source venv/bin/activate       # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000/`

---

## Usage

1. Fill in the candidate’s details in the form.
2. Submit the form.
3. The predicted candidate stage will be displayed on the page.

---

## Project Structure

```
CandidateProgress/
├── CandidateProgress/      # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── HireScope/              # Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── model.pkl           # Pre-trained ML model
├── templates/              # HTML templates
│   └── candidate_form.html
├── manage.py
└── requirements.txt
```

## Notes

* The ML model (`model.pkl`) is loaded **lazily** in `views.py` to prevent memory issues on server startup.
* Ensure the model file path in `views.py` matches your project directory.
* For production, consider using **PostgreSQL/MySQL** instead of SQLite.

## Dependencies

* Django
* pandas
* scikit-learn
* joblib
* numpy

Install all dependencies via:

pip install -r requirements.txt
