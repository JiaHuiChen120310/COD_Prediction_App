import joblib

# Load saved label encoders
label_encoders = joblib.load("label_encoders.pkl")

# Print all encoded categories
for col, encoder in label_encoders.items():
    print(f"\n🔹 Column: {col}")
    print("Categories:", list(encoder.classes_))  # Print all known values