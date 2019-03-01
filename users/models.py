from django.db import models
from django.urls import reverse
from django.shortcuts import render, redirect
# Create your models here.
class Permitidos(models.Model):
  email=models.EmailField(unique=True, max_length=254)
  
  def get_absolute_url(self):
      return reverse("users:detalhe", kwargs={"pk": self.pk})
  
  def __str__(self):
      return self.email
  class Meta:
      verbose_name_plural = 'Permitidos'
      
      