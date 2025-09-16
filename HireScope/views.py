from django.shortcuts import render
from .forms import CandidateForm
import joblib
import pandas as pd
import os

model = joblib.load("HireScope/ml_models/RandomForest_pipeline.pkl")

def candidate_input(request):
    prediction = None
    
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate_entry = form.save()  # Save to DB

             # Convert candidate data to DataFrame for the pipeline
            input_data = pd.DataFrame([{
                "Opportunity": candidate_entry.Opportunity,
                "Age": candidate_entry.Age,
                "Aggregate": candidate_entry.Aggregate,
                "NumCandidates": candidate_entry.NumCandidates,
                "Industry": candidate_entry.Industry,
                "Company": candidate_entry.Company,
                "Gender": candidate_entry.Gender,
                "Race": candidate_entry.Race,
                "Institution": candidate_entry.Institution,
                "Qualification": candidate_entry.Qualification,
                "Disciplines": candidate_entry.Disciplines,
            }])

            # Predict with the model
            prediction_result = model.predict(input_data)

            prediction_array = prediction_result[0]  

            stage = int(prediction_array[0])                # Stage number
            progress_score = round(float(prediction_array[1]), 2)  # Score rounded to 2 decimals

            prediction = f"Candidates predicted stage: {stage}, Predicted candidates progress score: {progress_score}"

    else:
        form = CandidateForm()
    
    return render(request, "candidate_form.html", {"form": form, "prediction": prediction})


def home(request):
    return render(request, "home.html")
