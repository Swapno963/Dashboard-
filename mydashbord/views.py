from rest_framework import generics
from .models import dashbordModel
from .serializers import MyModelSerializer
# Create your views here.

class DashbordView(generics.ListCreateAPIView):
    queryset = dashbordModel.objects.all()
    serializer_class = MyModelSerializer
