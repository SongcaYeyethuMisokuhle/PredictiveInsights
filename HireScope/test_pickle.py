import joblib

# Load the pipeline model
model = joblib.load('HireScope/ml_models/RandomForest_pipeline.pkl')
print("✅ Model loaded successfully!")
print(model)
