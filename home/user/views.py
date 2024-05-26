from django.http import HttpResponse


# Create your views here.
def hero(request):
    return HttpResponse("Hello, World!")