from django.db import models


# Create your models here.
class Product(models.Model):
    particulars = models.CharField(max_length=1000)
    rate        = models.DecimalField(decimal_places=2, max_digits=100,default=0)
    quantity    = models.DecimalField(decimal_places=2, max_digits=100,default=0)
    description = models.TextField()
