from django.db import models

class Sales(models.Model):
    name_of_sales   = models.CharField(max_length=30)
    profit          = models.FloatField()