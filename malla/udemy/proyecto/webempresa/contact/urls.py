from django.urls import path
from contact import views as contacts
urlpatterns = [
    # Paths del contact
    path('', contacts.contact, name="contactos"),
]