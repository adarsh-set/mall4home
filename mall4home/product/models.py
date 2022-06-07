from distutils.command.upload import upload
from itertools import product
from django.db import models

# Create your models here.
class pro_store(models.Model):
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField()
    p_image=models.ImageField(upload_to ='pic')
    p_desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.p_name
    
class comment(models.Model):
    product=models.ForeignKey(pro_store,related_name="comments",on_delete=models.CASCADE)
    u_name=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)