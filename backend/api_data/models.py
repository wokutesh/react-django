from django.db import models


class User(models.Model):
    name= models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(unique=True,blank=True)
    password=models.CharField(max_length=8)
    is_vendor=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


class Vender(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='vendor')
    bio=models.TextField()
    contact_details=models.TextField()
    bank_details=models.TextField()
    shipping_policy = models.TextField()
    return_policy = models.TextField()


class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='subcategories')


    def __str__(self):
        return self.name

class Product(models.Model):
    vender=

