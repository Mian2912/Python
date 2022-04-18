from operator import mod
import sqlite3
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
# forma de crear una tabla en la base de datos sqlite3
class Post (models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title