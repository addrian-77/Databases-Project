from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"Location in {self.country.name}"


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name


class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comments = models.TextField()

    def __str__(self):
        return f"Feedback for {self.project.project_name}"
