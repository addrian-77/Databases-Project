from django.db import models

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
