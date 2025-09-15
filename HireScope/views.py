from django.shortcuts import render
from .forms import CandidateForm

def candidate_input(request):
    prediction = None
    
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate_entry = form.save()  # Save to DB
            prediction = f"Details for Candidate {candidate_entry.candidate} saved. ML model will predict later."
    else:
        form = CandidateForm()
    
    return render(request, "candidate_form.html", {"form": form, "prediction": prediction})

def home(request):
    return render(request, "home.html")
