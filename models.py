from django.db import models

# Create your models here.
class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    userPass = models.CharField(max_length=100)

class Notes(models.Model):
    noteID = models.AutoField(primary_key=True)
    noteTitle = models.CharField(max_length = 50)
    noteBody = models.TextField()
    dateModified = models.DateField()
    userID = models.IntegerField()