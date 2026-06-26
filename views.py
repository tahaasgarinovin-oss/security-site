from django.shortcuts import render, redirect
from .models import Applicant

def apply(request):
    success = False

    if request.method == "POST":
        Applicant.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            phone=request.POST['phone'],
            experience=request.POST['experience']
        )
        success = True

    return render(request, 'apply.html', {"success": success})


def home(request):
    return render(request, 'home.html')