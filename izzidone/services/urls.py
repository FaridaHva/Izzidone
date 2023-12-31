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
    #Orders
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderRetrieveAPIView.as_view(), name='order-retrieve'),
    path('blogs/', views.BlogListAPIView.as_view(), name='blog-list'),
    path('blogs/create/', views.BlogCreateAPIView.as_view(), name='blog-create'),
    path('blog-details/', views.BlogDetailsListAPIView.as_view(), name='blog-details-list'),
    path('blog-details/<int:pk>/', views.BlogDetailsRetrieveAPIView.as_view(), name='blog-details-retrieve'),

    ]