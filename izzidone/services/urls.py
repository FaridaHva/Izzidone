from django.urls import path
from . import views

urlpatterns = [
    #Services
    path('services/', views.ServiceListCreateView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceRetrieveView.as_view(), name='service-detail'),
    path('subservices/', views.SubserviceListCreateView.as_view(), name='subservice-list'),
    path('subservices/<int:pk>/', views.SubserviceRetrieveView.as_view(), name='subservice-detail'),
    path('choose-services/', views.ChooseServiceListCreateView.as_view(), name='choose-service-list'),
    #Professionals
    path('professionals/', views.ProfessionalListCreateView.as_view(), name='professional-list-create'),
    path('professionals/<int:pk>/', views.ProfessionalRetrieveView.as_view(), name='professional-retrieve'),

    ]