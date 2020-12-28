from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    profileUser = models.OneToOneField(User, on_delete=models.CASCADE, max_length=200)
    email = models.CharField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Phone',blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='Address', blank=True, null=True)
    image = models.ImageField(verbose_name='Upload Image', blank=True, null=True, upload_to='profilePics/')
