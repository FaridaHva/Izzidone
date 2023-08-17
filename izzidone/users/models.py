from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
            

           

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30, )
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }


