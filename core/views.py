from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

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
