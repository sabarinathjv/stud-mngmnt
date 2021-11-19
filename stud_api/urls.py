from django.urls import path
from .views import StudLists,studDetail



urlpatterns = [

    path('', StudLists.as_view(), name='listcreate'),#studDetail
    path('<int:pk>/', studDetail.as_view(), name='detail'),

    
]