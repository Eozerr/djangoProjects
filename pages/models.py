from django.db import models


class Hasta(models.Model):
    tcno = models.CharField(max_length=11, primary_key=True,unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "register_hasta"

    
class Bolum(models.Model):
    bolumad = models.CharField(max_length=100)
    idbolum = models.IntegerField(primary_key=True,default=0)

    def __str__(self):
        return self.bolumad
    
    class Meta:
        db_table = "register_bolum"
    
class Doktor(models.Model):
    idDoktor=models.IntegerField(primary_key=True)
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    #Bolum_idbolum = models.ForeignKey(Bolum, on_delete=models.CASCADE)
    Bolum = models.ForeignKey(Bolum, on_delete=models.CASCADE, null=True, blank=True, related_name='doktorlar',db_column='Bolum_idbolum')
    sifre = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
    
    class Meta:
        db_table = "register_doktor"
        
        
class Randevu(models.Model):

    bolum = models.ForeignKey(Bolum,on_delete=models.CASCADE, null=True, blank=True, related_name='bolums',db_column='bolum')
    hastatcno = models.CharField(max_length=11,null=True)
    tarih = models.DateField()
    saat = models.TimeField()
    doktorid = models.ForeignKey(Doktor, on_delete=models.CASCADE, null=True, blank=True, related_name='doktorlar',db_column='doktorid')
    
    class Meta:
        db_table = "randevu"
        
    def __str__(self):
        return f"{self.bolum.bolumad} - {self.saat} - {self.tarih} - {self.hastatcno}"