from audioop import reverse
import imp
from xml.etree.ElementTree import fromstring
import django
from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {
           'posts': Post.objects.all(), 
    }
    print(context['posts'])
    return render(request, "blog/home.html", context)


hello = Post.objects.all()

print(hello)