from django.db import models

class Usuari(models.Model):
    email = models.EmailField(unique=True, max_length=50)  
    nom = models.CharField(max_length=20) 
    cognoms = models.CharField(max_length=20)  
    contrasenya = models.CharField(max_length=15) 
