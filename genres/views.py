from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Genre
from .serializers import GenreSerializer
from .permissions import GenrePermissionclass


class GenreCreateListView(generics.ListCreateAPIView):
      permission_classes = [IsAuthenticated, GenrePermissionclass]
      queryset = Genre.objects.all()
      serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
      permission_classes = [IsAuthenticated, GenrePermissionclass]
      queryset = Genre.objects.all()
      serializer_class = GenreSerializer
