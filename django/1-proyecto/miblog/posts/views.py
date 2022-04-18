from math import degrees
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

#Crear nuestras vistas
class HelloWorld(View) :
    def get(self, request):
        data = {
            'name' : 'Miguel',
            'last_name' : 'Herrera',
            'codes': ['java','JavaScript', 'Python']
        }
        return render(request, 'hello_world.html', context = data)

