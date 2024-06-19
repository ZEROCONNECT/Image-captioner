from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ImageDetailSerializer

from .models import ImageDetail
# Create your views here.
class ImageDetailViewSet(viewsets.ModelViewSet):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer
