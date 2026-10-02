from django.shortcuts import render
from . models import Student
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def students_list(request):
    students = Student.objects.all()
    return render(request, 'main/students.html', {'students': students})