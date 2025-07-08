from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SignUpForm

# Create your views here.

def landing(request):
    return render(request, 'landing.html', {'star_range': range(30), 'landing': True})

def upload(request):
    return render(request, 'upload.html')

def preprocessing(request):
    return render(request, 'preprocessing.html')

def superres(request):
    return render(request, 'superres.html')

def evaluation(request):
    return render(request, 'evaluation.html')

def results(request):
    return render(request, 'results.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    # signup logic
    pass

def login_view(request):
    # login logic
    pass

def profile(request):
    # profile logic
    pass
