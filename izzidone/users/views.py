from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_text
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer, ChangePasswordSerializer, EmailSerializer, ResetPasswordSerializer,UserProfileUpdateSerializer
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes


# RegisterAPI
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  # Queryset containing all User objects
    serializer_class = RegisterSerializer  
    
# LoginAPI
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)  # Create serializer instance with request data
        serializer.is_valid(raise_exception=True)  # Validate the serializer data, raise exception if invalid
        return Response(serializer.data, status=status.HTTP_200_OK)  
        
# LogoutAPI
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer  
    permission_classes = (permissions.IsAuthenticated,)  
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        serializer.save()  # Blacklist the refresh token to log out the user
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return successful response after logging out

# ChangePasswordAPI  
class ChangePasswordView(generics.UpdateAPIView):

    # API endpoint to change user's password.

    queryset = User.objects.all()  
    permission_classes = (IsAuthenticated,)  
    serializer_class = ChangePasswordSerializer  

# PasswordResetAPI
class PasswordReset(generics.GenericAPIView):

    # API endpoint to request a password reset link.

    serializer_class = EmailSerializer 

    def post(self, request):
        # Create token.
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            # Create reset URL
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            # Send the reset link as mail to the user.
            return Response(
                {
                    "message": f"Your password reset link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "User doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

# ResetPasswordAPI
class ResetPasswordAPI(generics.GenericAPIView):

    # API endpoint to verify token and reset user's password.

    serializer_class = ResetPasswordSerializer  

    def patch(self, request, *args, **kwargs):

        # Verify token & encoded_pk and then reset.
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)

        # Extract the user instance
        token = self.kwargs.get('token')
        encoded_pk = self.kwargs.get('encoded_pk')
        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)

        # Update the user's password
        password = serializer.validated_data['password']
        user.set_password(password)
        user.save()

        # Update the user profile
        profile_serializer = UserProfileUpdateSerializer(
            instance=user,
            data=request.data,
            partial=True
        )
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )

# UpdateProfileAPI
class UserProfileUpdateView(generics.UpdateAPIView):
    """
    API endpoint to update user profile information.
    """
    queryset = User.objects.all()  
    serializer_class = UserProfileUpdateSerializer  
    permission_classes = (IsAuthenticated,)  

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
