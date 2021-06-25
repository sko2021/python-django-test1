from django.http import HttpResponse
from django.shortcuts import render
from .models import UspsServices
import xml.etree.ElementTree as ET

def hello(request):

   #These objects will be fetched from the XML File
 xmldoc = minidom.parse('bpg.xml')
    root = xmldoc.getroot()
    serviceList = []
    for service in root.findall('service'):
        # get the service details
        serviceList.append(service)
        return render(request, 'bpgtemplate.html',{"serviceList":serviceList})
