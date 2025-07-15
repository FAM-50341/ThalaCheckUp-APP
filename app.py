import streamlit as st
import joblib
import pandas as pd

# Model load
stage1_model = joblib.load('stage1_voting_ensemble.pkl')
stage2_model = joblib.load('stage2_voting_ensemble.pkl')

def engineer_features(row):
    row['hb_div_mcv'] = row['hb'] / row['mcv']
    row['rbc_mul_mchc'] = row['rbc'] * row['mchc']
    row['mch_mul_mcv'] = row['mch'] * row['mcv']
    row['rdw_div_rbc'] = row['rdw'] / row['rbc']
    row['plt_div_wbc'] = row['plt'] / row['wbc']
    return row

def preprocess_user_input(user_input_list):
    feature_names = ['gender', 'hb', 'pcv', 'rbc', 'mcv', 'mch', 'mchc', 'rdw',
                     'wbc', 'neut', 'lymph', 'plt', 'hba', 'hba2', 'hbf']
    input_df = pd.DataFrame([user_input_list], columns=feature_names)
    input_df = engineer_features(input_df.iloc[0]).to_frame().T
    return input_df

def predict_alpha_thalassemia(user_input_list):
    processed_input = preprocess_user_input(user_input_list)
    stage1_pred = stage1_model.predict(processed_input)[0]
    if stage1_pred == 0:
        return "Normal: No thalassemia detected."
    stage2_pred = stage2_model.predict(processed_input)[0]
    if stage2_pred == 0:
        return "Carrier Gene Detected: The type is Silent Carrier"
    else:
        return "Carrier Gene Detected: The type is Alpha Trait"

st.title("ThalaCheckUp")
st.subtitle(" Multi-stage diagnostic tool that checks Alpha Thalassemia conditions from standard blood test parameters")

# User Inputs
gender = st.selectbox("Gender (0=Female, 1=Male)", [0,1])
hb = st.number_input("Hemoglobin (Hb)")
pcv = st.number_input("Packed Cell Volume (PCV)")
rbc = st.number_input("Red Blood Cell Count (RBC)")
mcv = st.number_input("Mean Corpuscular Volume (MCV)")
mch = st.number_input("Mean Corpuscular Hemoglobin (MCH)")
mchc = st.number_input("Mean Corpuscular Hemoglobin Concentration (MCHC)")
rdw = st.number_input("Red Cell Distribution Width (RDW)")
wbc = st.number_input("White Blood Cell Count (WBC)")
neut = st.number_input("Neutrophils (%)")
lymph = st.number_input("Lymphocytes (%)")
plt = st.number_input("Platelets (PLT)")
hba = st.number_input("Hemoglobin A (HbA)")
hba2 = st.number_input("Hemoglobin A2 (HbA2)")
hbf = st.number_input("Hemoglobin F (HbF)")


if st.button("Check"):
    user_input = [gender, hb, pcv, rbc, mcv, mch, mchc, rdw,
                  wbc, neut, lymph, plt, hba, hba2, hbf]
    result = predict_alpha_thalassemia(user_input)
    st.success(result)
