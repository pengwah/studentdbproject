from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import student

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        if request.POST['name']:
            searchname = request.POST['name']
            students = student.objects.filter(fullname__icontains=searchname)
            return render(request, 'students/home.html', {'students': students})
        else:
            return render(request, 'students/home.html')
    else:
        return render(request, 'students/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['birthdate'] and request.POST['email'] :
            if request.POST['id']:
              Student = get_object_or_404(student, pk=request.POST['id'])
            else:
                Student = student()
            Student.firstname = request.POST['firstname']
            Student.lastname = request.POST['lastname']
            Student.birthdate = request.POST['birthdate']
            Student.email = request.POST['email']
            Student.phone1 = request.POST['phone1']
            Student.phone2 = request.POST['phone2']
            Student.fullname = Student.firstname + " " + Student.lastname
            Student.street = request.POST['street']
            Student.city = request.POST['city']
            Student.zipcode = request.POST['zipcode']
            Student.save()
            return redirect('/students/' + str(Student.id))
        else:
          return render(request, 'students/create',{'error':'All fields are requied'})
    else:
        return render(request, 'students/create.html')


@login_required
def detail(request, student_id):
    Student = get_object_or_404(student, pk=student_id)
    return render(request, 'students/detail.html',{'student':Student})
