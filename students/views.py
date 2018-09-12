from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.views import generic
from .models import student
from .models import studentinstrument
from .models import instrument
from .models import *
import json

# Create your views here.
@login_required
def home(request):
    Instruments = instrument.objects.filter()
    Instructors = instructor.objects.filter()
    studentInstruments = studentinstrument()
    instructorObj = None
    instrumentObj = None
    Studenturl = []

    if request.method == 'POST':
        # print('instrument id', request.POST.get('instrument'))
        # print('instructor id', request.POST.get('instructor'))

        if request.POST['searchstring']:
            searchname = request.POST['searchstring']
            if searchname == '*':
                searchname = ''
            # students = student.objects.filter(fullname__icontains=searchname)
            if request.POST.get('instrument') or request.POST.get('instructor'):
                studentInstruments = studentinstrument.objects.all()
                if request.POST.get('instrument'):
                    instrumentObj = get_object_or_404(instrument, pk= request.POST.get('instrument'))
                    if instrumentObj:
                        studentInstruments = studentInstruments.filter(instrument=instrumentObj)
                if request.POST.get('instructor'):
                    instructorObj = get_object_or_404(instructor, pk= request.POST.get('instructor'))
                    if instructorObj:
                        studentInstruments = studentInstruments.filter(instructor=instructorObj)

                students = student.objects.filter(pk__in=studentInstruments.values('student'), fullname__icontains=searchname)
            else:
                students = student.objects.filter(fullname__icontains=searchname)
            # if request.POST.get('instrument'):
            #     instrumentObj = get_object_or_404(instrument, pk= request.POST.get('instrument'))
            #
            #     if instrumentObj:
            #         studentInstruments = studentinstrument.objects.filter(student__in=students, instrument=instrumentObj).values('student')
            #         students = student.objects.filter(pk__in=studentInstruments)
            # if request.POST.get('instructor'):
            #     instructorObj = get_object_or_404(instructor, pk= request.POST.get('instructor'))
            #     if instructorObj:
            #         studentInstruments = studentinstrument.objects.filter(student__in=students, instructor=instructorObj).values('student')
            #         students = student.objects.filter(pk__in=studentInstruments)
            for studentobj in students:
                Studenturl.append(studentobj.get_absolute_url())

            Studentjson = serializers.serialize("json", students)
            Instrumentsjson = serializers.serialize("json", Instruments)
            Instructorsjson = serializers.serialize("json", Instructors)
            data = [{
                'student':Studentjson,
                'studenturl':Studenturl,
                'instruments':Instrumentsjson,
                'instructors':Instructorsjson,
                }]
            if request.is_ajax():
                return HttpResponse(json.dumps(data), content_type="application/json")
            else:
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
            if request.is_ajax():
                data = [{
                    }]
                return HttpResponse(json.dumps(data), content_type="application/json")
            else:
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
def refresh(request):
    # Student = get_object_or_404(student, pk=request.POST['id'])
    Student = student.objects.filter(pk=request.POST['id'])
    StudentInstrument = studentinstrument.objects.filter(student_id=request.POST['id'])
    Instruments = instrument.objects.filter()
    Instructors = instructor.objects.filter()
    Studentjson = serializers.serialize("json", Student)
    StudentInstrumentjson = serializers.serialize("json", StudentInstrument)
    Instrumentsjson = serializers.serialize("json", Instruments)
    Instructorsjson = serializers.serialize("json", Instructors)
    data = [{
        'student':Studentjson,
        'studentinstrument':StudentInstrumentjson,
        'instruments':Instrumentsjson,
        'instructors':Instructorsjson
        }]
    return HttpResponse(json.dumps(data), content_type="application/json")

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
        # print('instrument id', request.POST.get('instrument'))
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
