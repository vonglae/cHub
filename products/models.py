from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PRODUCT(models.Model):
    product_name=models.CharField(default='产品名称',max_length=50)
    introduction=models.TextField(default='产品介绍')
    product_linked=models.CharField(default='http://',max_length=100)
    icon=models.ImageField(default='xixi.jpg',upload_to='images/')
    picture=models.ImageField(default='xixi.jpg',upload_to='images/')
    product_date=models.DateField()
    votes=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name