from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.


class ElfbarList(generics.ListAPIView):
    queryset = Elfbar.objects.all()
    serializer_class = ElfbarSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['charge']
    ordering_fields = ['price']


class ElfbarGet(generics.RetrieveAPIView):
    queryset = Elfbar.objects.all()
    serializer_class = ElfbarSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Elfbar.objects.get(slug=slug)


class ElfbarGetTastes(generics.ListAPIView):
    queryset = Elfbar.objects.all()
    serializer_class = ElfbarSerializer

    def get_queryset(self):
        charge = self.kwargs.get('charge')
        return Elfbar.objects.filter(charge=charge)
