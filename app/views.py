from django.shortcuts import render
from app.views import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():

         return HttpResponse('student form is inserted successfully')
    return render(request,'Student.html',d)
