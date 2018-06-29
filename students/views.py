from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import student

# Create your views here.
@login_required
def home(request):
    return render(request, 'students/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['firstname'] and request.POST['middlename'] and request.POST['lastname'] and request.POST['birthdate'] and request.POST['email'] :
            Student = student()
            Student.firstname = request.POST['firstname']
            Student.middlename = request.POST['middlename']
            Student.lastname = request.POST['lastname']
            Student.birthdate = request.POST['birthdate']
            Student.email = request.POST['email']
            Student.save()
            return redirect('home')
        else:
          return render(request, 'students/create',{'error':'All fields are requied'})
    else:
        return render(request, 'students/create.html')
