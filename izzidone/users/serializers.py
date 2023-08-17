from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.urls import reverse
from django.core.mail import send_mail
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from typing import Dict


# RegisterSerializer
class RegisterSerializer(serializers.ModelSerializer):
    # Serializer for user registration
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'name', 'surname')
        extra_kwargs = {
            'name': {'required': True},
            'surname': {'required': True}
        }

    def validate(self, attrs):
        # Validate password fields
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        # Create a new user instance
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            surname=validated_data['surname']
        )

        # Set user's password and save
        user.set_password(validated_data['password'])
        user.save()

        return user


# LoginSerializer
class LoginSerializer(serializers.ModelSerializer):
    # Serializer for user login
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=255)
    tokens = serializers.SerializerMethodField()
    
    def get_tokens(self, obj) -> Dict[str, str]:
        # Get user's JWT tokens
        user = User.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    
    class Meta:
        model = User
        fields = ['password', 'email', 'tokens']
    
    def validate(self, attrs):
        # Validate user's credentials
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {
            'email': user.email,
            'tokens': user.tokens
        }


# LogoutSerializer
class LogoutSerializer(serializers.Serializer):
    # Serializer for user logout
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        # Validate the refresh token
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        # Blacklist the refresh token
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


# ChangePasswordSerializer
class ChangePasswordSerializer(serializers.ModelSerializer):
    # Serializer for changing user's password
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        # Validate password fields
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        # Validate old password for change
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        # Update user's password
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


# EmailSerializer
class EmailSerializer(serializers.Serializer):
    # Serializer for requesting a password reset email.
    email = serializers.EmailField()

    class Meta:
        fields = ("email",)


# ResetPasswordSerializer
class ResetPasswordSerializer(serializers.Serializer):
    # Serializer for resetting a user's password.
    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")

    def validate(self, data):
        # Verify token and encoded_pk and then set new password
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data

# UpdateProfileSerializer
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    # Serializer for updating user's profile information
    class Meta:
        model = User
        fields = ('name', 'surname')