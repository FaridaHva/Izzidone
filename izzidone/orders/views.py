from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,) 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
