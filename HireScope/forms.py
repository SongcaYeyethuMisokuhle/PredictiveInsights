from django import forms
from .models import CandidateEntry

class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateEntry
        fields = [
            "industry", "company", "opportunity", "candidate",
            "gender", "age", "race", "institution", "aggregate",
            "qualification", "disciplines", "num_candidates"
        ]