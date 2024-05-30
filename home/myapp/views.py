from django.shortcuts import render,redirect
from .models import Post
from django.conf import settings
from .models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def home(request):
    hero = SliderItem.objects.all()
    post_grid = Post.objects.all()
    current_data = datetime.now()
    context={
        'hero':hero,
        'current_data':current_data,
        'post_grid':post_grid,
    }
    return render(request,'index.html',context )

def single_post(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'single-post.html', context)

def categories(request):
    return render(request, 'category.html')

def about(request):
    about = AboutBlog.objects.all()
    teams = OurTeamName.objects.all()
    context = {
        'blog':about,
        'teams':teams
    }

    return render(request, 'about.html',context)

def contact(request):
    info = personal_info.objects.all() #Fetch all data from databasae fetch means data is coming from databasae to dispay in templates.
    # infos = personal_info.objects.filter(name="parsuram")
    # This is for form
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        address = request.POST.get('address')
        roles = request.POST.get('roles')
        desc = request.POST.get('desc')
        phone_number = request.POST.get('phone_number')

        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        if contact:
            print("You message have been submitetd successfully!!")
    return render(request, 'contact.html', {'info':info})


def profile(request):
    return render(request, 'profile.html')


def payment(request):
    return render(request,'payment.html')