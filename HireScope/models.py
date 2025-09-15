from django.db import models

# Create your models here.

class CandidateEntry(models.Model):
    industry = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    opportunity = models.IntegerField()
    candidate = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    age = models.IntegerField()
    race = models.CharField(max_length=50)
    institution = models.CharField(max_length=200)
    aggregate = models.IntegerField()
    qualification = models.CharField(max_length=200)
    disciplines = models.CharField(max_length=200)
    num_candidates = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Candidate {self.candidate} - {self.industry} ({self.aggregate})"
