# Blog Rating Module

## Directory Structure 
```
blog-rating-app/
├── backend/                          # Django backend
│   ├── blog_backend/                # Django project root
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── blog_api/                    # Django app
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                # Blog, User, Comment models
│   │   ├── serializers.py           # DRF serializers
│   │   ├── views.py                 # API views
│   │   ├── urls.py                  # API routes
│   │   └── permissions.py
│   ├── manage.py
│   └── requirements.txt            # Backend dependencies
│
├── frontend/                        # Angular frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/          # blog form, blog list, etc.
│   │   │   ├── services/            # blog.service.ts
│   │   │   ├── models/              # Blog.ts, User.ts
│   │   │   └── app.module.ts
│   │   ├── assets/
│   │   ├── environments/
│   │   └── index.html
│   ├── angular.json
│   ├── package.json
│   └── tsconfig.json
│
├── rating_engine/                  # AI-based rating module
│   ├── __init__.py
│   ├── rate.py                     # Main rating script
│   ├── model/                      # If ML model is saved
│   │   └── rating_model.pkl
│   └── utils.py                    # Text preprocessing, etc.
│
├── .gitignore
├── README.md
└── run.sh                         # Optional: script to run full stack
```