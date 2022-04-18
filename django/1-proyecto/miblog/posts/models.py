from turtle import title
from django.db import models

# por medio de este modelo se va a crear una tabla con el orm django
class Post(models.Model) :
    title = models.CharField(max_length=250) #cuando queremos limitar el texto
    description = models.TextField() #cunado no queremos limitar el texto
    order = models.IntegerField() # orden en que se va creando
    created_at = models.DateTimeField(auto_now_add=True) # va crear la fecha actual automaticamente