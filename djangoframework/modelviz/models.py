
from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=10)


class Item(models.Model):
    MONTH_CHOICES = (
    ("JAN", "January"),
    ("FEB", "February"),
    ("MAR", "March"),
    ("DE", "December"),
)
    name = models.ForeignKey(Data,on_delete=models.CASCADE)
    gender = models.CharField(max_length=3,choices=MONTH_CHOICES)
    