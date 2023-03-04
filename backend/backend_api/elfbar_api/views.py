from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .models import *
from .serializers import *

# Create your views here.


class ElfbarList(generics.ListAPIView):
    queryset = Elfbar.objects.all()
    serializer_class = ElfbarSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['price']


class ElfbarGet(generics.RetrieveAPIView):
    queryset = Elfbar.objects.all()
    serializer_class = ElfbarSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Elfbar.objects.get(slug=slug)
