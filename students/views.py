from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import student
from .models import studentinstrument
from .models import instrument
from .models import *

# Create your views here.
@login_required
def home(request):
    Instruments = instrument.objects.filter()
    Instructors = instructor.objects.filter()
    studentInstruments = studentinstrument()

    if request.method == 'POST':
        print('instrument id', request.POST.get('instrument'))
        print('instructor id', request.POST.get('instructor'))


        if request.POST['name']:
            searchname = request.POST['name']
            if searchname == '*':
                searchname = ''
            students = student.objects.filter(fullname__icontains=searchname)
            if request.POST.get('instrument'):
                instrumentObj = get_object_or_404(instrument, pk= request.POST.get('instrument'))
                if instrumentObj:
                    studentInstruments = studentinstrument.objects.filter(student__in=students, instrument=instrumentObj).values('student')
                    students = student.objects.filter(pk__in=studentInstruments)
            if request.POST.get('instructor'):
                instructorObj = get_object_or_404(instructor, pk= request.POST.get('instructor'))
                if instructorObj:
                    studentInstruments = studentinstrument.objects.filter(student__in=students, instructor=instructorObj).values('student')
                    students = student.objects.filter(pk__in=studentInstruments)

            return render(request, 'students/home.html', {'students': students, 'instruments':Instruments, 'instructors':Instructors})
        else:
            return render(request, 'students/home.html', {'instruments':Instruments, 'instructors':Instructors})
    else:
        return render(request, 'students/home.html', {'instruments':Instruments, 'instructors':Instructors})

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
            Student.email2 = request.POST['email2']
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
    StudentInstrument = studentinstrument.objects.filter(student_id=student_id)
    Instruments = instrument.objects.filter()
    Instructors = instructor.objects.filter()
    return render(request, 'students/detail.html',{'student':Student, 'studentinstrument':StudentInstrument, 'instruments':Instruments, 'instructors':Instructors})

@login_required
def delinstrument(request):
    if request.POST['student_id']:
        Student = get_object_or_404(student, pk=request.POST['student_id'])
    if  request.POST['studentinstrument_id']:
        StudentInstrument = get_object_or_404(studentinstrument, pk=request.POST['studentinstrument_id'])
        if StudentInstrument:
            StudentInstrument.delete()
    return redirect('/students/' + str(Student.id))

def addinstrument(request):
    if request.POST['student_id']:
        print('instrument id', request.POST.get('instrument'))
        Student = get_object_or_404(student, pk=request.POST['student_id'])
        Instrument = get_object_or_404(instrument, pk= request.POST.get('instrument'))
        Instructor = get_object_or_404(instructor, pk= request.POST.get('instructor'))
        if Student and Instrument and Instructor:
            StudentInstrument = studentinstrument()
            StudentInstrument.student = Student
            StudentInstrument.instrument = Instrument
            StudentInstrument.instructor = Instructor
            StudentInstrument.save()
        return redirect('/students/' + str(Student.id))
