from django.db import models

# Create your models here.
class Iqar(models.Model):
    registered_number = models.CharField(max_length=200,  unique=True)
    location = models.CharField(max_length=200)
    area = models.IntegerField()
    contents = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    date_owned = models.DateField()
    currencies = models.CharField(max_length=200)
    value_1 = models.DecimalField(max_digits=200, decimal_places=2)
    value_2 = models.DecimalField(max_digits=200, decimal_places=2)
    def __str__(self):
      return "Iqar %s"%self.registered_number
