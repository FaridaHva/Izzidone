from django.urls import path
from .views import ServiceListCreateView, ServiceRetrieveView, ServiceDestroyView, SubserviceListCreateView, SubserviceRetrieveView, SubserviceDestroyView, ChooseServiceListCreateView

urlpatterns = [
    path('services/', ServiceListCreateView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceRetrieveView.as_view(), name='service-detail'),
    path('services/<int:pk>/destroy/', ServiceDestroyView.as_view(), name='service-destroy'),  
    path('subservices/', SubserviceListCreateView.as_view(), name='subservice-list'),
    path('subservices/<int:pk>/', SubserviceRetrieveView.as_view(), name='subservice-detail'),
    path('subservices/<int:pk>/destroy/', SubserviceDestroyView.as_view(), name='subservice-destroy'),  
    path('choose-services/', ChooseServiceListCreateView.as_view(), name='choose-service-list'),
    ]