from django.shortcuts import render, get_object_or_404
from .models import Pages
# Create your views here.
def page(request, pages_id, page_slug):
    page = get_object_or_404(Pages, id = pages_id)
    return render(request, 'pages/sample.html', {'pages': page})