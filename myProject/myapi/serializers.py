#serializers.py
from rest_framework import serializers
from .models import Hero, Villian

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class VillianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villian
        fields = ('name', 'alias')