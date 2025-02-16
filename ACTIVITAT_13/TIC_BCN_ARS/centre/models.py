from django.db import models


class Students(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    email = models.EmailField()
    curs = models.CharField(max_length=100)
    moduls = models.CharField(max_length=100)


class Teacher(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    email = models.EmailField()
    curs = models.CharField(max_length=200)  
    tutor = models.CharField(max_length=2)
    moduls = models.CharField(max_length=200) 



