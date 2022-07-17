from django.shortcuts import render

from . models import pastPaper
from . serializers import pastpaperSerializer
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
    def get(self, request, board, subject, year, month, nq):
        try:
            allMCQs = pastPaper.objects.filter(board=board, subject=subject, year=year, month=month)
        except pastPaper.DoesNotExist:
            raise Http404
        if len(allMCQs) > nq:
            allMCQs = allMCQs[:nq]
        serializer = pastpaperSerializer(allMCQs, many=True)
        return Response(serializer.data)
