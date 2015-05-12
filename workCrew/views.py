#from django.shortcuts import render
import docCreator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    docCreator.docCreator()
   
    
    return render(request, 'workCrew/downloadSchedules.html')

def allergies(request):
    output = "placeholder"
    return HttpResponse(output)