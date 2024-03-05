from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def created_user(self, username, email, password):
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email="admin@admin.uz"):
        user = self.created_user(username, email, password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=40, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to="image/", null=True)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser
