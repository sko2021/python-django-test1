from django.http import HttpResponse
from django.shortcuts import render
from .models import UspsServices
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.dom.minidom import parse,parseString,Document
import os
def hello(request):

   #These objects will be fetched from the XML File
 xmldoc = ET.parse('bpg.xml')
 root = xmldoc.getroot()
 service = UspsServices()
 serviceList = []
 for child in root:
    # print(child.tag,child.attrib)
     print(child.attrib['serviceName'])
     serviceList.extend
     service.serviceName = child.attrib['serviceName']
     service.serviceDescription = child.attrib['serviceDescription']
     service.accessFlag = child.attrib['accessFlag']
     service.id = child.attrib['id']
     serviceList[int(service.id)-1]=service

 print(serviceList[0].serviceName)
 print(serviceList[1].serviceName)
 return render(request, 'bpgtemplate.html',{"serviceList":serviceList})
