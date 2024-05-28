from django.urls import path
from Login import views
# from django.contrib.auth import views as auth_views  #logout
from .views import logout_view


urlpatterns = [
    path('login/', views.login_page, name = 'login_page'),
    path('register/', views.register_page, name='register'),
    #logout lai function call garesi pughyo 
    # path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),
]