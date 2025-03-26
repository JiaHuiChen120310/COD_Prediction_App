import pandas as pd
import xgboost as xgb
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load Excel Data
df = pd.read_excel("COD_testrun2.xlsx")

# **Step 1: Define All Possible Chemicals (Including "nan")**
chemical_list = [
    "H2SO4", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
    "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
    "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
    "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "nan"  # 🔹 Ensure "nan" is included
]

# **Step 2: Strip Extra Spaces in Dataset and Replace Empty Cells with "nan"**
for col in ['chem1', 'chem2', 'chem3', 'chem4', 'chem5', 'chem6']:
    df[col] = df[col].astype(str).str.strip().replace("", "nan")  # Convert missing values to "nan"

# **Step 3: Train LabelEncoders Using the Same List for All Chemicals**
label_encoders = {}
for col in ['chem1', 'chem2', 'chem3', 'chem4', 'chem5', 'chem6']:
    le = LabelEncoder()
    le.fit(chemical_list)  # Ensure "nan" is in the encoder
    df[col] = df[col].apply(lambda x: x if x in chemical_list else "nan")  # Replace unseen with "nan"
    df[col] = le.transform(df[col])  # Encode values
    label_encoders[col] = le  # Store encoder

# Encode `Sector` separately
sector_le = LabelEncoder()
df['Sector'] = sector_le.fit_transform(df['Sector'])
label_encoders["Sector"] = sector_le  # Store the sector encoder

# Select features & target
X = df.drop(columns=['cod(after)'])  # Features
y = df['cod(after)']  # Target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model & label encoders
joblib.dump(model, 'xgboost_cod_model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

# Model evaluation
y_pred = model.predict(X_test)
print(f"R² Score: {r2_score(y_test, y_pred)}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred))}")
print(f"MAE: {mean_absolute_error(y_test, y_pred)}")
