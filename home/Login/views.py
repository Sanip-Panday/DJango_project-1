from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        #Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            #display an error message if username doesnot exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        
        #Authenticate the user with the provided username and password
        user1 = authenticate(request, username=username, password=password)

        if user1 is not None:
            # Log in the user and redirect to home page upon successful login
            login(request, user1)
            return redirect('home')
        else:
            # Display an error message if authentication fails
            messages.error(request, "Invalid username or password")
            return redirect('/login/')

    #Render the login page  template(Get request)
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # Redirect to the login page or any other desired page
    return redirect('login_page')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if a user with provided username already exists
        user = User.objects.filter(username=username)

        if not User.objects.filter(username=username):
            # message.info(request, "Username already exists")
            # return redirect('/register/')

        #Create a new User object with provided information
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username
            )

            #Set the user's password and save the user object
            user.set_password(password)
            user.save()

            #Display an information message indicating successful account creations
            messages.info(request, "Account created Successfully!")
            return redirect('login_page')

    return render(request, 'register.html')

