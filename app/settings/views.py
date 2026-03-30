from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        return Response({'name' : 'Hello Geeks'})
    
class About(APIView):
    def get(self, request):
        return Response({'name' : 'This is about page'})

class Contacts(APIView):
    def get(self, request):
        return Response({'name': 'Contacts page', 'phone': '+996 555 212 293', 'email': 'info@geeks.kg'})