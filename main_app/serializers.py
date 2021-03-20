from rest_framework import serializers, fields
from .models import Food_Pack


class Food_Pack_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Pack
        fields = ['pk', 'user', 'title', 'description', 'categories', 'timestamp', 'is_halal', 'is_kosher', 'is_vegan']

