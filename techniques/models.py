from django.db import models

class ConservationTechnique(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WaterTip(models.Model):
    tip = models.CharField(max_length=200)

    def __str__(self):
        return self.tip
