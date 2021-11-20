from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# Create your models here.

class user_data(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200,blank=False,null=True)
    contact=models.CharField(max_length=20,blank=False,null=True)
    def __str__(self):
        return self.user.username
    
    

class image(models.Model):
	username = models.CharField(max_length=100)
	imgname = models.CharField(max_length=100)
	category = models.CharField(max_length=100,null=True,blank=True)
	img = ResizedImageField(size=[800, 600],quality=100,upload_to='images/')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class women(models.Model):
#     productId=models.CharField(max_length=200,blank=False,null=True)
#     productName=models.CharField(max_length=200,blank=False,null=True)
#     image=models.CharField(max_length=200,blank=False,null=True)
#     price=models.IntegerField(blank=False,null=True)
#     brand=models.CharField(max_length=200,blank=True,null=True)
#     discription=models.TextField(blank=True,null=True)
#     def __str__(self):
#         return self.productId
    
# class men(models.Model):
#     productId=models.CharField(max_length=200,blank=False,null=True)
#     productName=models.CharField(max_length=200,blank=False,null=True)
#     image=models.CharField(max_length=200,blank=False,null=True)
#     price=models.IntegerField(blank=False,null=True)
#     brand=models.CharField(max_length=200,blank=True,null=True)
#     discription=models.TextField(blank=True,null=True)
#     def __str__(self):
#         return self.productId    

# class kids(models.Model):
#     productId=models.CharField(max_length=200,blank=False,null=True)
#     productName=models.CharField(max_length=200,blank=False,null=True)
#     image=models.CharField(max_length=200,blank=False,null=True)
#     price=models.IntegerField(blank=False,null=True)
#     brand=models.CharField(max_length=200,blank=True,null=True)
#     discription=models.TextField(blank=True,null=True)
#     def __str__(self):
#         return self.productId        

# class cart(models.Model):
#     productId=models.CharField(max_length=200,blank=False,null=True)
#     customerId=models.CharField(max_length=200,blank=False,null=True)
#     productName=models.CharField(max_length=200,blank=False,null=True)
#     image=models.CharField(max_length=200,blank=False,null=True)
#     cost=models.IntegerField(blank=False,null=True)
 
#     def __str__(self):
#         return self.productId   