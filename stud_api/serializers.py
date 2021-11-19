from rest_framework import serializers
from stud_api.models import StudentDetail


class StudSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'age', 'standard', 'english', 'physics','maths','chemistry','biology','history','geography']
        model = StudentDetail