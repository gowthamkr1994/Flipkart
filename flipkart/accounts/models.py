from django.db import models

# Create your models here.
class Signup(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="",primary_key=True)
    password = models.CharField(max_length=8, default="")
    contact = models.CharField(max_length=12, default="")
    address = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.email


# class Meta():
#     Verbose_name_plural="Products"
