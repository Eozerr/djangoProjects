from django.db import models


class Hasta(models.Model):
    tcno = models.CharField(max_length=11, primary_key=True)
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = "register_hasta"
        
class Doktor(models.Model):
    sifre = models.CharField(max_length=45)
    ad = models.CharField(max_length=45)
    class Meta:
        db_table = "doktor"
        
    def __str__(self):
        return self.ad
