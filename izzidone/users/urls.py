from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    path('update-profile/', views.UserProfileUpdateView.as_view(), name='update-profile'),




]