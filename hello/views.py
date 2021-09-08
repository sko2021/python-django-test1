from django.http import HttpResponse
from django.shortcuts import render
from .models import UspsServices

def hello(request):
   serviceList = UspsServices.objects.all() 
   return render(request, 'bpgtemplate.html',{"serviceList":serviceList})
