from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .forms import SignUpForm, CustomAuthenticationForm

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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/dashboard/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/dashboard/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
