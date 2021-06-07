# heros-djangotutorial
django tutorial from Bennet Garner

continue tutorial:
https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c


1. Set up django
    pip install django
    django-admin startproject myProject
    cd myProject
    python manage.py runserver
    
    python manage.py startapp myapi // create an api for the new app
    4. tell django to recognize the new app we just craeted
        - edit myProject/settings.py to include 'myapi'
    5. migrate the database
        python manage.py migrate
    6. create superuser
        python manage.py createsuperuser

2. Create a model in the database that Django ORM will manage
    1. build myapi/models.py (add a Hero)
    2. make migrations
        python manage.py makemigrations
        python manage.py migrate
    3. register Hero with admin site
        myapi/admin.py --> add admin.site.register(Hero)
    4. create new Heros

3. Set up Django REST framework
    pip install djangorestframework

    then tell django that we installed REST framework in 
        myProject/settings.py

        INSTALLED_APPS = [
        'rest_framework',
        'myapi',
        ...

4. Serialize the Hero model
    - need to tell REST framework about Hero model and how it should serialize the data
    - serialization==process of converting a Model to JSON
    - using a serializer, we can specify what fields should be present in the JSON representation of the model
    - the serializer will turn the heros into a JSON representation so the API users can parse them (even if they are not using Python)
    - when user POST's JSON data to the API, serilzier will convert that JSON to a Hero model for us to save or validate
Need to create a new file--myapi/serializers.py
    1. import the Hero model
    2. import the REST framework serializer
    3. create a new class that links the Hero with its serializer