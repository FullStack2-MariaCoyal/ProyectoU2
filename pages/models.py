from django.db import models

# Create your models here.

class PostSurvivor(models.Model):
    tipos = (
        ('S', 'Superviviente'),
        ('M', 'Monstruo'),
    )
    tipo = models.CharField(default="" ,max_length=1, choices=tipos)
    Name = models.CharField(max_length=255)
    age = models.DateField()
    description = models.TextField(default="")
    image = models.ImageField(upload_to='static/img/')
    def __str__(self):
        return self.tipo

class PostMonster(models.Model):
    tipos = (
        ('S', 'Superviviente'),
        ('M', 'Monstruo'),
    )
    tipo = models.CharField(default="",max_length=1, choices=tipos)
    Name = models.CharField(max_length=255)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='static/img/')
    def __str__(self):
        return self.tipo