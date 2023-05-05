from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    logo = models.FileField()
    president = models.CharField(max_length=50)
    murabbiy = models.CharField(max_length=50)
    yil = models.DateField()
    eng_katta_tr = models.CharField(max_length=50)
    eng_katta_sotuv = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nom}"

class Player(models.Model):
    ism = models.CharField(max_length=50)
    pozitsiya = models.CharField(max_length=50)
    millat = models.CharField(max_length=50)
    tr_narx = models.CharField(max_length=50)
    tug_yil = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}"

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='sotganlari')
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE)
    narx = models.CharField(max_length=50)
    tax_narx =  models.CharField(max_length=50, null=True, blank=True)
    mavsum =  models.CharField(max_length=50)
    def __str__(self):
        return f"{self.player}"

class HozirgiMavsum(models.Model):
    mavsum = models.CharField(max_length=7)
    def __str__(self):
        return f"{self.mavsum}"