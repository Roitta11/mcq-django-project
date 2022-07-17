from dataclasses import fields
from rest_framework import serializers
from . models import pastPaper

class pastpaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = pastPaper
        fields='__all__'
