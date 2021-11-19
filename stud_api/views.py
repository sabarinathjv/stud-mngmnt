from rest_framework import generics
from stud_api.models import StudentDetail
from .serializers import StudSerializer
from rest_framework.views import APIView
from rest_framework.response  import Response
from django_filters import rest_framework as filters



class StudLists(generics.ListCreateAPIView):    
    queryset = StudentDetail.objects.all()
    serializer_class = StudSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['age','name']

class studDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = StudSerializer










