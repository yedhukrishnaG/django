from django.db import models # type: ignore

# Create your models here.
class Basicinfo(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=5,default='M')
    value = models.BooleanField()

class Dashboard(models.Model):
    article_number = models.CharField(max_length=50)
    article_title = models.CharField(max_length=50)
    stock_level = models.CharField(max_length=50)
    earliest_expiration_date = models.CharField(max_length=50)
    batch_amount = models.CharField(max_length=50)
    reorder_level = models.CharField(max_length=50)
    maximum_level  = models.CharField(max_length=50)
