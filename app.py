import streamlit as st
import pandas as pd
from predict import predict_cod_after

st.title("COD Prediction App")

# Create user input form
with st.form("prediction_form"):
    sector = st.selectbox("sector",["nan", "Biofuels", "Chemical logistics", "Chemical production", 
                                    "Dairy", "Dairy food/wastewater", "Farming", "Fish (Shrimps processing)", "Fish processing", 
                                    "Food", "Food industry", "Food/ wastewater", "Laundry", "PFAS", "PFAS Removal", "Paper", 
                                    "Paper recycling", "Plastic", "RWZI", "Steel", "Wastewater", "Wastewater treatment", 
                                    "Water treatment Algae", "coatings", "waste management", "Beverages/Waste water"])
    sector = "nan" if sector.strip() == "" else sector
    cod_before = st.number_input("COD Before Treatment", min_value=0.0, step=0.0001, format="%.6f")
    
    chem1 = st.selectbox("Chemical 1", ["nan", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
                                        "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
                                        "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
                                        "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "H2SO4"])
    chem1 = "nan" if chem1.strip() == "" else chem1
    chem1_dose = st.number_input("Chemical 1 Dose", min_value=0.0, step=0.0001, format="%.6f")

    chem2 = st.selectbox("Chemical 2", ["nan", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
                                        "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
                                        "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
                                        "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "H2SO4"])
    chem2 = "nan" if chem2.strip() == "" else chem2
    chem2_dose = st.number_input("Chemical 2 Dose", min_value=0.0, step=0.0001, format="%.6f")

    chem3 = st.selectbox("Chemical 3", ["nan", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
                                        "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
                                        "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
                                        "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "H2SO4"])
    chem3 = "nan" if chem3.strip() == "" else chem3
    chem3_dose = st.number_input("Chemical 3 Dose", min_value=0.0, step=0.0001, format="%.6f")

    chem4 = st.selectbox("Chemical 4", ["nan", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
                                        "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
                                        "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
                                        "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "H2SO4"])
    chem4 = "nan" if chem4.strip() == "" else chem4
    chem4_dose = st.number_input("Chemical 4 Dose", min_value=0.0, step=0.0001, format="%.6f")

    chem5 = st.selectbox("Chemical 5", ["nan", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
                                        "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
                                        "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
                                        "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "H2SO4"])
    chem5 = "nan" if chem5.strip() == "" else chem5
    chem5_dose = st.number_input("Chemical 5 Dose", min_value=0.0, step=0.0001, format="%.6f")

    chem6 = st.selectbox("Chemical 6", ["nan", "HClO", "FeCl3", "FerSol", "Poly", "NaOH", "KFerSol", "PAC", "Iron Sulphate",
                                        "CaOH", "H2O2", "HNO3", "KH2PO4", "VTA", "VAT", "CTAB", "APG", "M40", "Al2(SO4)3",
                                        "Al(SO4)3", "HCl", "Fe2(SO4)3", "NaSi", "CH3COOH", "FeSO4", "NaClO", "CaO", "RP34",
                                        "SDS", "Na-EDTA", "Combiphos L7", "HB-5265", "Ferric 40%", "H2SO4"])
    chem6 = "nan" if chem6.strip() == "" else chem6
    chem6_dose = st.number_input("Chemical 6 Dose", min_value=0.0, step=0.0001, format="%.6f")

    submit = st.form_submit_button("Predict COD After Treatment")

    if submit:
        # Prepare input data
        input_data = {
            "Sector": sector, "cod(before)": cod_before,
            "chem1": chem1, "chem1 dose": chem1_dose,
            "chem2": chem2, "chem2 dose": chem2_dose,
            "chem3": chem3, "chem3 dose": chem3_dose,
            "chem4": chem4, "chem4 dose": chem4_dose,
            "chem5": chem5, "chem5 dose": chem5_dose,
            "chem6": chem6, "chem6 dose": chem6_dose
        }

        print("\n📝 User Input Data:")
        print(input_data)

        # Predict
        prediction = predict_cod_after(input_data)

        # Display result
        st.success(f"Predicted COD After Treatment: {prediction:.6f}")
