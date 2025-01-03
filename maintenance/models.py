from django.db import models

class MaintenanceRecord(models.Model):
    technology = models.ForeignKey('technologies.Technology', on_delete=models.CASCADE)

    def __str__(self):
        return f"Maintenance Record for {self.technology.name}"
