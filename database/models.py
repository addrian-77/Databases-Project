from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stakeholder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FundingSource(models.Model):
    source_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.source_name}: {self.amount}"


class Regulation(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class ConservationTechnique(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WaterTip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.CharField(max_length=200)

    def __str__(self):
        return self.tip
    

class AboutMessages(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Title: {self.title}, message: {self.message[:30]}..."
    

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    customization_form = models.TextField()

    def __str__(self):
        return self.category_name
    

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    description = models.TextField()
    goals = models.TextField()
    water_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    additional_customization = models.TextField()

    def __str__(self):
        return self.project_name


class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comments = models.TextField()
    def __str__(self):
        return f"Feedback for {self.project.project_name}"


class TechnologyImplemented(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.technology.name} at {self.project.project_name}"


class TechnologyTechnique(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    technique = models.ForeignKey(ConservationTechnique, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.technology.name} - {self.technique.name}"

class MaintenanceRecord(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f"Maintenance Record for {self.technology.name}"

class TrainingProgram(models.Model):
    program_name = models.CharField(max_length=100)

    def __str__(self):
        return self.program_name


class ResearchStudy(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class WaterSource(models.Model):
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return self.source_name


class UsageData(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

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
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Energy Consumption for {self.technology.name}: {self.value}"
