from django.urls import path
from pages import views as pages

urlpatterns = [
    # Paths del blog
    path('<int:pages_id>/<slug:page_slug>', pages.page, name='pages'),
]