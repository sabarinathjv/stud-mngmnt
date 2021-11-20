from rest_framework import generics
from stud_api.models import StudentDetail
from .serializers import StudentDetailSerializer
from django_filters import rest_framework as filters



#rqst       # http://127.0.0.1:8000/    #post
# {
#     "name":"sabari",
#     "age":24,
#      "standard":10,
#      "marks":[{"name":"physics","marks":15},{"name":"chemistry","marks":10},{"name":"hindi","marks":30}]


# }


class StudLists(generics.ListCreateAPIView):    
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['age','name',"standard"]

class studDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer










