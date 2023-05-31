from rest_framework import serializers
from .models import ColCity

class ColCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ColCity
        fields = "__all__"