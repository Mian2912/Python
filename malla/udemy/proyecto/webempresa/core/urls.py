from django.urls import path
from core import views as core
urlpatterns = [
    # Paths del core
    path('', core.home, name="Inicio"),
    path('about/', core.about, name="Acerca de"),
    path('visitanos/', core.store, name="visitanos"),
]