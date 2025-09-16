from django.db import models

# Create your models here.

class CandidateEntry(models.Model):
    Full_name = models.CharField(max_length=255, null=True, blank=True)
    Industry = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Opportunity = models.IntegerField()
    Gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    Age = models.IntegerField()
    Race = models.CharField(max_length=50)
    Institution = models.CharField(max_length=200)
    Aggregate = models.IntegerField()
    Qualification = models.CharField(max_length=200)
    Disciplines = models.CharField(max_length=200)
    NumCandidates = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Industry} ({self.Aggregate})"
