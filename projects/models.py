from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    secondaryImages = models.ImageField(upload_to='images/')
    ThirdImages = models.ImageField(upload_to='images/')
    tools = models.TextField()
    about = models.TextField()
    learn = models.TextField()
    extra = models.TextField()



    def __str__(self):
        return self.summary

class ArtImages(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name



class ComputerScienceP(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    secondaryImages = models.ImageField(upload_to='images/')
    ThirdImages = models.ImageField(upload_to='images/')
    tools = models.TextField()
    about = models.TextField()
    learn = models.TextField()


    def __str__(self):
        return self.name

class Eproject(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    secondaryImages = models.ImageField(upload_to='images/')
    ThirdImages = models.ImageField(upload_to='images/')
    tools = models.TextField()
    about = models.TextField()
    learn = models.TextField()

    def __str__(self):
        return self.name

class Lproject(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    tools = models.TextField()
    about = models.TextField()
    learn = models.TextField()

    def __str__(self):
        return self.name

