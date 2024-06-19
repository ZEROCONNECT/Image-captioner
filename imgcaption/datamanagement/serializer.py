from rest_framework import serializers
from .models import ImageDetail
class ImageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageDetail
        fields = "__all__"
        read_only_fields = ("id","created_at")
