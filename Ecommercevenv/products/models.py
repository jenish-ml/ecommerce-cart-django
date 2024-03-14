from django.db import models
from category.models import *

# Create your models here.
class Product(models.Model):
    LIVE =1
    DELETE = 0
    DELETE_CHOICES =((LIVE,'Live'),(DELETE,'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='uploads')
    priority = models.IntegerField(default = 0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=DELETE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title