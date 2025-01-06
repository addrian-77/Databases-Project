from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class TechnologyImplemented(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    date = models.DateField()
    country = models.ForeignKey('projects.Country', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.technology.name} at {self.project.project_name}"


class TechnologyTechnique(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    technique = models.ForeignKey('techniques.ConservationTechnique', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.technology.name} - {self.technique.name}"
