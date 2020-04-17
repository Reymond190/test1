from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StatusSerializer
from .models import Status


class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


