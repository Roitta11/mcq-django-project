from django.shortcuts import render

from . models import pastPaper
from . serializers import pastPaperSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

'''
To-do:
    - Understand the code, read the documentation religiously
    - Extend the functionality for each of the endpoints listed similarly
    - Improve the naming
    - Make a separate url for the papers app
'''


# nq --> number of questions ( only to limit the questions in the response)
# Endpoint 1 --> /mcq/board/subject/year/month/variant/nq
class getOnePaper(APIView):
    def get(self, request, board, subject, year, month, variant, nq):
        try:
            allMCQs = pastPaper.objects.filter(board=board, subject=subject, year=year, month=month, variant = variant)
        except pastPaper.DoesNotExist:
            raise Http404
        if len(allMCQs) > nq:
            allMCQs = allMCQs[:nq]
        serializer = pastPaperSerializer(allMCQs, many=True)
        return Response(serializer.data)

# Endpoint 2 -> mcq/board/subject/year/month/variant/question-number
class getEndpointTwo(APIView):
    def get(self, request, board, subject, year, month, variant, questionNum):
        credentials = pastPaper.objects.filter(board = board, subject = subject, year = year, month = month, variant = variant,     
        questionNum = questionNum)
        serializer = pastPaperSerializer(credentials, many = True)
        return Response(serializer.data)


# Endpoint 3 --> mcq/board/subject/topic/number-of-questions
class getEndpointThree(APIView):
    def get(self, request, board, subject, topic, nq):
        try:
            allMCQs = pastPaper.objects.filter(board=board, subject=subject, topic = topic)
        except pastPaper.DoesNotExist:
            raise Http404
        if len(allMCQs) > nq:
            allMCQs = allMCQs[:nq]
        serializer = pastPaperSerializer(allMCQs, many=True)
        return Response(serializer.data)



# Endpoint 4 --> mcq/board/subject/number-of-questions
class getEndpointFour(APIView):
    def get(self, request, board, subject, nq):
        try:
            allMCQs = pastPaper.objects.filter(board=board, subject=subject)
        except pastPaper.DoesNotExist:
            raise Http404
        if len(allMCQs) > nq:
            allMCQs = allMCQs[:nq]
        serializer = pastPaperSerializer(allMCQs, many=True)
        return Response(serializer.data)


    