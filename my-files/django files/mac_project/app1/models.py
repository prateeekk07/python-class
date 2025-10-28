from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=25)
    mobile = models.BigIntegerField(null=True)

    class Meta:
        db_table = "test_model"

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    