from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'PolitiSearch/home.html')

def about(request):
    return render(request, 'PolitiSearch/about.html')
