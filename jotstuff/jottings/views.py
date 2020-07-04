from django.shortcuts import render
from rest_framework import generics
from .serializers import JottingSerializer
from .models import Jotting

# Create your views here.
class JottingList(generics.ListAPIView):
  queryset = Jotting.objects.all()
  serializer_class = JottingSerializer

# To help with CRUD operation
class JottingDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Jotting.objects.all()
  serializer_class = JottingSerializer
