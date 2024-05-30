from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/', views.single_post, name='single_post'),
    path('category/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('profile/', views.profile, name = 'profile'),
      path('payment/', views.payment, name = 'payment'),

]

    

