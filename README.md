Photo Library 📸

A full-stack Photo Library web application where users can upload, manage, and categorize their photo collections. Includes AI-based tagging and search features.
Features

    🖼️ Upload and manage photos
    🏷️ Categorize photos by tags and categories
    🔍 AI-based auto-tagging
    🗂️ User-friendly frontend (React)
    🔧 RESTful API backend (Django REST Framework)
    🐘 PostgreSQL database

Tech Stack

    Frontend: React, Tailwind CSS
    Backend: Django, Django REST Framework
    Database: PostgreSQL
    AI Integration: Python-based models for auto-tagging
    Containerization: Docker (optional)

Setup Instructions

    Clone the repo

git clone https://github.com/ecvignesh/photo_library.git
cd photo_library

Backend setup

cd backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Frontend setup

cd frontend
npm install
npm start
