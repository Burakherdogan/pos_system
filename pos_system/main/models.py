from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50, null=True)
    image = models.FileField(upload_to="images", blank=True)
    
    