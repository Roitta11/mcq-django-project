from dataclasses import fields
from rest_framework import serializers
from . models import pastPaper

class pastPaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = pastPaper
        fields='__all__'
