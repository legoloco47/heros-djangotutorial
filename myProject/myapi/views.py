from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, VillianSerializer
from .models import Hero, Villian

from django.http import HttpResponse


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class VillianViewSet(viewsets.ModelViewSet):
    queryset = Villian.objects.all().order_by('name')
    serializer_class = VillianSerializer



def see_both_sides(request):
    message = f'Insert how many heroes and how many villians you have'
    return HttpResponse