from rest_framework import serializers
from .models import Col

class ColSerializer(serializers.ModelSerializer):
    class Meta:
        model = Col
        fields = "__all__"