from django.urls import path
from blog import views as blog
urlpatterns = [
    # Paths del blog
    path('', blog.blog, name="blog"),
    path('category/<int:category_id>/', blog.category, name='category')
]