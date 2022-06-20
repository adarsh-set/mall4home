from django.db import models

from product.models import pro_store



class comment (models.Model):
    product=models.ForeignKey(pro_store,related_name="comments",on_delete=models.CASCADE)
    u_name=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)