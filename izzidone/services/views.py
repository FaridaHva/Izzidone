from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  
from .models import Service, Subservice, ChooseService, Professional, Order
from .serializers import ServiceSerializer, SubserviceSerializer, ChooseServiceSerializer,  ProfessionalSerializer, OrderSerializer


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubserviceListCreateView(generics.ListCreateAPIView):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer

class SubserviceRetrieveView(generics.RetrieveAPIView):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer

class ChooseServiceListCreateView(generics.ListCreateAPIView):
    queryset = ChooseService.objects.all()
    serializer_class = ChooseServiceSerializer



#Professionals

class ProfessionalListCreateView(generics.ListCreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalListCreateView(generics.ListCreateAPIView):
    queryset = Professional.objects.filter()
    serializer_class = ProfessionalSerializer


class ProfessionalRetrieveView(generics.RetrieveAPIView):
    queryset = Professional.objects.filter()
    serializer_class = ProfessionalSerializer


#Orders

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.filter() 
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,) 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
