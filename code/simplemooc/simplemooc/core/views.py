from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'usuario': 'fulano de tal', 'hw': 'Hello World'})
