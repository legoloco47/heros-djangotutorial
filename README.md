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
        ```
        #serializers.py
        from rest_framework import serializers
        from .models import Hero

        class HeroSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Hero
                fields = ('name', 'alias')
        ```
5. Display the Data
    - wire up the uRLs and views to display the data
    1. need to render the different heroes in JSON format
        - to do this we need to
            1. Query the database for all heros
            2. pass that database queryset into the serializer we just created
                - it will get converted to JSON and rendered
        In myapi/views.py

            ```
            from django.shortcuts import render
            from rest_framework import viewsets
            from .serializers import HeroSerializer
            from .models import Hero


            # Create your views here.
            class HeroViewSet(viewsets.ModelViewSet):
                queryset = Hero.objects.all().order_by('name')
                serializer_class = HeroSerializer
            ```
        - ModelViewSet is a special view that Django Rest Framework provides
            - it will handle GET and POST for Heros without us having to do more work
    2. Site URLs
        in django, URLs get resolved at the project level first. start with file myProject/urls.py
        - add the URL for our API (for now put the URL at the index)    - added: path('', include('myapi.urls'))
    3. API URLs
        - we have to add a path in myapi/urls.py
            ```
            from django.urls import include, path
            from rest_framework import routers
            from . import views

            router = routers.DefaultRouter()
            router.register(r'heroes', views.HeroViewSet)

            # wire up our API using automatic URL routing
            # Additionally, we include login URLs for the browsable API
            urlpatterns = [
                path('', include(router.urls)),
                path('api-auth/', include('rest_framework.urls', namespace='rest_Framework'))
            ]
            ```

        - we added "router" imported from "rest_framework"
            - REST framework router will make sure our requests end up at the right resource dynamically
                - if we add or delete items from the database, the URLs will update to match. 
        - a router works with a "viewset" (i.e views.py) to dynamically route requests. for a "router" to work, it needs to point to a viewset
    as an exercise create villians!

    Test it out
        visit the endpoint via GET
        GET /heros/

My steps:
1. Create Villian model in myapi/models.py
2. Create Villian ViewSet in myapi/views.py
2. Create Villian serializer in myapi/serializer.py
3. Add Villians to router in myapi/urls.py 