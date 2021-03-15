from django.db import models

# Create your models here.

class PostSurvivor(models.Model):
    survivorName = models.CharField(max_length=255)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='bd/img/')
    def __str__(self):
        return self.survivorName

class PostMonster(models.Model):
    monsterName = models.CharField(max_length=255)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='bd/img/')
    def __str__(self):
        return self.monsterName