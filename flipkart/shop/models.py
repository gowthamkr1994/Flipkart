from django.db import models
import datetime
# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=500, default="")
    subcategory = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    pubdate = models.DateField()

    def __str__(self):
        return self.name

