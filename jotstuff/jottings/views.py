from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import JottingSerializer
from .models import Jotting
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class JottingList(generics.ListCreateAPIView):
  permission_class = (IsOwnerOrReadOnly,)
  queryset = Jotting.objects.all()
  serializer_class = JottingSerializer

# To help with CRUD operation
class JottingDetail(generics.RetrieveUpdateDestroyAPIView):
  # Since we only want to grant the owner write-abilities
  permission_class = (IsOwnerOrReadOnly,)
  queryset = Jotting.objects.all()
  serializer_class = JottingSerializer
