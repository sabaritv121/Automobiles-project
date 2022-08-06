from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def store(request):
    return render(request, 'store.html')

def index(request):
    return render(request, 'index.html')

def aaaAdmin(request):
    return render(request, 'aaaAdmin.html')