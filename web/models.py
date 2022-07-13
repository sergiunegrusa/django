from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length=required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    summary = models.TextField(default="this is cool")