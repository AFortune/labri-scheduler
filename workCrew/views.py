#from django.shortcuts import render
import docCreator
from django.http import HttpResponse
# Create your views here.
def index(request):
    docCreator.docCreator()
   
    output = 'success'
    return HttpResponse(output)

def allergies(request):
    output = "placeholder"
    return HttpResponse(output)