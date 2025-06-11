from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to="static/images",null=True,blank=True)
    title=models.CharField(max_length=300)
    content=models.CharField(max_length=300)
    cost=models.IntegerField()
    def __str__(self):
        return self.title
    

class Products(models.Model):
    cate_name=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name="Products")
    pic=models.ImageField(upload_to="static/images",null=True,blank=True)
    title=models.CharField(max_length=300)
    content=models.CharField(max_length=300)
    cost=models.IntegerField()
    def __str__(self):
        return f"{self.title}-{self.cost}"


class Images_product(models.Model):
    img_more=models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True,related_name="images")
    images=models.ImageField(upload_to="media/static/images",null=True,blank=True)
    def __str__(self):
        return self.img_more.title

