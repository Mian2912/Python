from distutils.command.upload import upload
from enum import auto
from pydoc import describe
from tabnanny import verbose
from turtle import title, update
from django.db import models

# Create your models here.
class Project(models.Model):
    title =  models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    urlField = models.URLField(verbose_name="Direccion web" ,null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now= True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-create"]

    def __str__(self) -> str:
        return self.title