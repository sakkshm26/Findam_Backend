from django.db import models

# Create your models here.
class Blockchain(models.Model):
    name = models.CharField(max_length=50)
    org = models.CharField(max_length=15)
    rating = models.FloatField()
    certificate = models.BooleanField()
    desc = models.TextField()
    link = models.CharField(max_length=200)
    
class Cs(models.Model):
    name = models.CharField(max_length=50)
    org = models.CharField(max_length=15)
    rating = models.FloatField()
    certificate = models.BooleanField()
    desc = models.TextField()
    link = models.CharField(max_length=200)

class Electronics(models.Model):
    name = models.CharField(max_length=50)
    org = models.CharField(max_length=15)
    rating = models.FloatField()
    certificate = models.BooleanField()
    desc = models.TextField()
    link = models.CharField(max_length=200)

class Entrepreneurship(models.Model):
    name = models.CharField(max_length=50)
    org = models.CharField(max_length=15)
    rating = models.FloatField()
    certificate = models.BooleanField()
    desc = models.TextField()
    link = models.CharField(max_length=200)

class Web3(models.Model):
    name = models.CharField(max_length=50)
    org = models.CharField(max_length=15)
    rating = models.FloatField()
    certificate = models.BooleanField()
    desc = models.TextField()
    link = models.CharField(max_length=200)