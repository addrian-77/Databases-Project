from django.db import models

class WaterSource(models.Model):
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return self.source_name


class UsageData(models.Model):
    technology = models.ForeignKey('technologies.Technology', on_delete=models.CASCADE)
    location = models.ForeignKey('projects.Location', on_delete=models.CASCADE)

    def __str__(self):
        return f"Usage of {self.technology.name} at {self.location}"


class ClimateData(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Temperature: {self.temperature}"


class SoilData(models.Model):
    ph_level = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Soil pH: {self.ph_level}"


class EnergyConsumption(models.Model):
    technology = models.ForeignKey('technologies.Technology', on_delete=models.CASCADE)

    def __str__(self):
        return f"Energy Consumption for {self.technology.name}"
