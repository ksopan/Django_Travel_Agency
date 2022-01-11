from django.db import models

# Create your models here.

# class Destination:
#     id: int
#     name: str
#     img: str
#     desc: str
#     price: int
#     offer: bool

# For Database Model creation
class Destination(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    
    
class Detailed_desc(models.Model):
    dest_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=20)
    days = models.IntegerField(default=5)
    price = models.IntegerField(default=20000)
    rating = models.IntegerField(default=5)
    dest_name = models.CharField(max_length=25)
    img1=models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    desc = models.TextField()
    day1= models.CharField(max_length=200)
    day2 = models.CharField(max_length=200)
    day3 = models.CharField(max_length=200)
    day4 = models.CharField(max_length=200)
    day5 = models.CharField(max_length=200)
    day6 = models.CharField(max_length=200)