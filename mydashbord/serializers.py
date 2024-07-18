from rest_framework import serializers
from .models import dashbordModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = dashbordModel
        fields = '__all__'
