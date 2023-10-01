from django.db import models

class login(models.Model):
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=100)
