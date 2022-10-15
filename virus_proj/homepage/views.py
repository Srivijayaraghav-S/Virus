from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'homepage/index.html')


def academics(request):
    return render(request, 'homepage/academics.html')


def past(request):
    return render(request, 'homepage/past-recruiters.html')


def contact(request):
    return render(request, 'homepage/contact.html')
