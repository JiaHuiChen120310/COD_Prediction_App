import pandas as pd
import joblib
import xgboost as xgb

# Load Model & Encoders
model = joblib.load("xgboost_cod_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

def predict_cod_after(input_data):
    input_df = pd.DataFrame([input_data])

    # Encode categorical variables
    for col in ['Sector', 'chem1', 'chem2', 'chem3', 'chem4', 'chem5', 'chem6']:
        input_df[col] = input_df[col].astype(str)
        input_df[col] = label_encoders[col].transform(input_df[col])

    # Fill missing numerical values
    for col in ['cod(before)', 'chem1 dose', 'chem2 dose', 'chem3 dose', 'chem4 dose', 'chem5 dose', 'chem6 dose']:
        input_df[col] = input_df[col].fillna(0)

    # Make prediction
    return model.predict(input_df)[0]
