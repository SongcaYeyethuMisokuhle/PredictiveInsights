from django.shortcuts import render
import requests
from .forms import CandidateForm
import joblib
import pandas as pd
import os

MODEL_PATH = "HireScope/ml_models/RandomForest_pipeline.pkl"
MODEL_URL = "https://drive.google.com/uc?export=download&id=18cTgMn2g3p2OH7AOK54hrLSRoRfDgms_"

# Ensure model exists locally
if not os.path.exists(MODEL_PATH):
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    print("Downloading model...")
    r = requests.get(MODEL_URL, allow_redirects=True)
    with open(MODEL_PATH, "wb") as f:
        f.write(r.content)

model = joblib.load(MODEL_PATH)

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
