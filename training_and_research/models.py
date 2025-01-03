from django.db import models

class TrainingProgram(models.Model):
    program_name = models.CharField(max_length=100)

    def __str__(self):
        return self.program_name


class ResearchStudy(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
