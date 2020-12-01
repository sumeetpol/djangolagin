from django.db import models
from datetime import datetime,date
# Create your models here.
class mainsignup(models.Model):
    sid=models.TextField(null=True)
    fname=models.TextField(null=True,max_length=200)
    mname=models.TextField(null=True,max_length=200)
    lname=models.TextField(null=True,max_length=200)
    image=models.ImageField(null=True,upload_to='img')
    image1=models.ImageField(null=True,upload_to='img')
    image2=models.ImageField(null=True,upload_to='img')
    gender=models.TextField(null=True,max_length=200)
    dobdate=models.DateField( null=True,auto_now=False, auto_now_add=False)
    sd=models.TextField(null=True,max_length=200)
    age=models.TextField(null=True,max_length=200)
    height=models.TextField(null=True,max_length=200)
    education=models.TextField(null=True,max_length=500)
    job=models.TextField(null=True,max_length=500)
    cname=models.TextField(null=True,max_length=200)
    sname=models.TextField(null=True,max_length=200)
    dname=models.TextField(null=True,max_length=200)
    phno1=models.BigIntegerField(null=True,)
    phno2=models.BigIntegerField(null=True,)
    religion=models.TextField(null=True,max_length=200)
    rashi=models.TextField(null=True,max_length=200)
    income=models.TextField(null=True,max_length=200)


    def __str__(self):
        return self.fname

class Signup(models.Model):
    fname=models.TextField(null=True,max_length=200)
    lname=models.TextField(null=True,max_length=200)
    gender=models.TextField(null=True,max_length=200)
    date=models.DateField( null=True,auto_now=False, auto_now_add=False)
    email=models.EmailField(null=True,)
    phno1=models.BigIntegerField(null=True,)
    password=models.TextField(null=True,max_length=200)

    def __str__(self):
        return self.email
    
class Multiimage(models.Model):
    image1=models.ImageField(null=True,upload_to='imgmulti')

    def __str__(self):
        return self.image1  

class Fav_list(models.Model):
    mid=models.BigIntegerField(null=True,)
    statusid=models.BigIntegerField(null=True,)
    supid=models.BigIntegerField(null=True,)

    def __str__(self):
        return self.mid  