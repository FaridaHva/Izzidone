from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  
from .models import Service, Subservice, ChooseService
from .serializers import ServiceSerializer, SubserviceSerializer, ChooseServiceSerializer

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDestroyView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubserviceListCreateView(generics.ListCreateAPIView):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer

class SubserviceRetrieveView(generics.RetrieveAPIView):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer

class SubserviceDestroyView(generics.DestroyAPIView):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer

class ChooseServiceListCreateView(generics.ListCreateAPIView):
    queryset = ChooseService.objects.all()
    serializer_class = ChooseServiceSerializer