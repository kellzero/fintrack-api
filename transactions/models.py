from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  name = models.CharField(max_length=255)
  value = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateField()
  type = models.CharField(max_length=10)

  def __str__(self):
    return self.name