from django.shortcuts import render

from . models import pastPaper
from . serializers import pastpaperSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from papers import serializers

# Endpoint 3 --> Board/Subject/Topic/NumberOfQuestion
class getTopic(APIView):
    def get(self, request, format = None):
        getBoard = pastPaper.objects.all()
        serializer = pastpaperSerializer(getBoard,  
        many=True)
        return Response(serializer.data)

# Create your views here.

# endpoint 1


# class getOnePaper(APIView):
#     pass

# endpoint 2 

# class 

# endpoint 3

# class getTopic(APIView):
#     def get(self, request, format = None):
#         getBoard = pastPaper.objects.all()
#         serializer = pastpaperSerializer(getBoard,  
#         many=True)
#         return Response(serializer.data)


# # endpoint 4

# class getSubject(APIView):
#     def get(self, request, format = None):
#         getBoard = pastPaper.objects.all()
#         serializer = pastpaperSerializer(getBoard,  
#         many=True)
#         return Response(serializer.data)

