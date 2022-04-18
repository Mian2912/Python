from cgitb import html
from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, "blog/home.html", {'posts': posts})

def post (request, id):
    print(id)
    post = Post.objects.get(id = id)
    return render(request, 'blog/post.html', {'post': post})