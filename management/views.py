import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict

from . models import Student
from . forms import StudentForm

def index(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            item = form.save(commit=False)
            item.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request, 'management/index.html', {
        "Student_form" : StudentForm,
        "all_students" : Student.objects.all()
    })

def get_all_students(request):
    students = serializers.serialize("json", Student.objects.all())
    data = json.loads(students)
    return JsonResponse({"student" : data}, safe=False)

def get_single_student(request, pk):
    get_student = serializers.serialize("json", Student.objects.filter(id=pk))
    data = json.loads(get_student)
    return JsonResponse({"student": data[0]}, safe=False)
   
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return HttpResponse("Success")

