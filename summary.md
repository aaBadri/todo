- create project: `django-admin startproject Todo`
- run project: `python manage.py runserver`
- migrate: `python manage.py migrate`
- create super user: `python manage.py createsuperuser`
- create app: `python manage.py startapp home`
  - add urls.py file
  - add app to settings.py of Todo app
- add url: add app base url to Todo app urls.py then add all urls to app urls.py
- add template:
  - create template folder in root
  - add name.html
  - add name.html to settings.py: TEMPLATES -> 'DIRS': [BASE_DIR/"templates"]
  - return render(request, "name")
- templates [https://docs.djangoproject.com/en/5.0/topics/templates/]:
  - Variables
  - Tags
  - Filters
  - Comments
- models:
  - make migration: `python manage.py makemigrations`
  - migrate:  `python manage.py migrate`
- admin:
  - add model to admin.py
  - add to admin page: admin.site.register(Todo)

- CORS:
  -  pipenv install django-cors-headers
  -  Next update our django_project/settings.py file in three places:
    • add corsheaders to the INSTALLED_APPS
      "corsheaders",
    • add CorsMiddleware above CommonMiddleWare in MIDDLEWARE
      "corsheaders.middleware.CorsMiddleware",
    • create a CORS_ALLOWED_ORIGINS config at the bottom of the file
      CORS_ALLOWED_ORIGINS = (
          "http://localhost:3000",
          "http://localhost:8000",
      )

CSRF:
  At the bottom of the settings.py file, next to CORS_ORIGIN_WHITELIST, add this additional line for React’s default local port of 3000:
    CSRF_TRUSTED_ORIGINS = ["localhost:3000"]


- Depolyment: 
  We will again deploy the Django API backend with Heroku. Our deployment checklist includes:
  • configure static files and install WhiteNoise
    mkdir static
    pipenv install whitenoise
    WhiteNoise must be added to django_project/settings.py in the following locations:
      • whitenoise above django.contrib.staticfiles in INSTALLED_APPS 
        "whitenoise.runserver_nostatic",
      • WhiteNoiseMiddleware above CommonMiddleware
        "whitenoise.middleware.WhiteNoiseMiddleware",
      • STATICFILES_STORAGE configuration pointing to WhiteNoise under STATIC_URL = "/static/"
        STATICFILES_DIRS = [BASE_DIR / "static"]
        STATIC_ROOT = BASE_DIR / "staticfiles"
        STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
      python manage.py collectstatic
  • install Gunicorn as the production web server
    - pipenv install gunicorn
  • create requirements.txt, runtime.txt, and Procfile files
  • update the ALLOWED_HOSTS configuration