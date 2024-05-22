from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SliderItem
from .models import Post

from django.conf import settings
from .models import Contact


def home(request):
    return render(request,'index.html')

def single_post(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'single-post.html', context)

def categories(request):
    return render(request, 'category.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        if contact:
            print("You message have been submitetd successfully!!")
    return render(request, 'contact.html')

