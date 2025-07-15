# 🩸 ThalaCheck: Alpha Thalassemia Diagnosis Assistant

ThalaCheck is a machine learning-powered two-stage diagnostic tool that predicts Alpha Thalassemia conditions from standard blood test parameters. It supports early detection and classification into:
- Normal (Healthy individual)
- Silent Carrier
- Alpha Trait Carrier

🔬 Built with Streamlit for an intuitive interface, this app is a valuable aid for both patients and healthcare professionals.
## 🚀 Live App

👉 [ThalCheckUp](https://thalacheckup-app-1.onrender.com/)

## 📌 How It Works

### 🧪 Input Parameters:

Users input 15 blood-related features:
- `Gender` (0 = Male, 1 = Female)
- `Hemoglobin (Hb)`
- `Packed Cell Volume (PCV)`
- `Red Blood Cell count (RBC)`
- `Mean Corpuscular Volume (MCV)`
- `Mean Corpuscular Hemoglobin (MCH)`
- `Mean Corpuscular Hemoglobin Concentration (MCHC)`
- `Red Cell Distribution Width (RDW)`
- `White Blood Cell count (WBC)`
- `Neutrophil Count`
- `Lymphocyte Count`
- `Platelet Count (PLT)`
- `Hemoglobin A (HbA)`
- `Hemoglobin A2 (HbA2)`
- `Hemoglobin F (HbF)`

## 🧠 Models Used

This project uses a robust two-stage machine learning pipeline, combining multiple models and techniques to maximize classification performance:

🔹 Stage 1: Normal vs. Carrier Classification
Goal: Detect whether a person is Normal or an Alpha Thalassemia Carrier.

Model Type: Soft Voting Ensemble

Algorithms Used:

1. Logistic Regression

2. Decision Tree Classifier

3. Random Forest Classifier

4. XGBoost Classifier

Stage 2: Carrier Classification – Silent vs. Alpha Trait

Goal: For individuals predicted as Carriers in Stage 1, further classify into:

- Silent Carrier

- Alpha Trait Carrier

Model Type: Same as Stage 1 — Soft Voting Ensemble with tuned versions of:

- Logistic Regression

- Decision Tree

- Random Forest

- XGBoost

 ## 🩸 Why It Matters:
  
Alpha Thalassemia is a hereditary condition often underdiagnosed due to subtle symptoms, especially in silent carriers.

Early and accurate classification (Normal vs. Carrier → Silent vs. Alpha Trait) is essential for:

Family planning & genetic counseling

Preventing severe thalassemia in offspring

Reducing unnecessary anxiety or interventions

