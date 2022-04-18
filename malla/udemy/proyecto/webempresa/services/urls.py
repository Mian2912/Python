from django.urls import path
from services import views 

urlpatterns = [
    # Paths del services
    path('services/', views.services, name="servicios"),
]