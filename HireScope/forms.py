from django import forms
from .models import CandidateEntry

class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateEntry
        fields = [
            "Industry", "Company", "Opportunity",
            "Gender", "Age", "Race", "Institution", "Aggregate",
            "Qualification", "Disciplines", "NumCandidates"
        ]