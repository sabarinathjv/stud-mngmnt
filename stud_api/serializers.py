from rest_framework import serializers
from stud_api.models import StudentDetail,Mark






class MarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = [ 'name','marks']
        model = Mark

class StudentDetailSerializer(serializers.ModelSerializer):
    marks=MarkSerializer(many=True)

    class Meta:
        fields = [ 'name', 'age', 'standard','marks']
        model = StudentDetail

    def create(self, validated_data):
        stud_data = validated_data.pop('marks')
        stud_obj = StudentDetail.objects.create(**validated_data)
        for temp_data in stud_data:
            Mark.objects.create(**temp_data)
        return stud_obj











