from distutils.command.upload import upload
from django.db import models

# Create your models here.
class pro_store(models.Model):
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField()
    p_image=models.ImageField(upload_to ='pic')
    p_desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)