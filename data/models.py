from django.db import models

# Create your models here.

class data1_book(models.Model):
    ISBN = models.IntegerField(max_length=10)
    Title = models.CharField(max_length=50)
    AuthorID = models.IntegerField(max_length=10)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.CharField(max_length=20)
    PublishDate = models.DateField(max_length=8)
    Price = models.FloatField(max_length=10)

class data1_author(models.Model):
    AuthorID = models.IntegerField(max_length=10)
    Name = models.CharField(max_length=30)
    Age = models.IntegerField(max_length=5)
    Country = models.CharField(max_length=30)