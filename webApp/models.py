from django.db import models

class Calculation(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField()
