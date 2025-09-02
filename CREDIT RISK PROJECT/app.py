
# This is to install streamlint


# This will be for the main application!
import streamlit as st
import pandas as pd
import joblib

# Then to load the already dumped model
model = joblib.load("extra_trees_credit_model.pkl")

encoders = {col : joblib.load(f"{col}_encoder.pkl") for col in ["Sex", "Housing", "Saving accounts", "Checking account"] }

st.title("Credit Risk Prediction Application - Usman's Learning")
st.write("Enter applicant information to predict if the credit risk is good")

# This is to derive the age
age = st.number_input("Age", min_value = 18, max_value = 80, value = 30)
sex = st.selectbox("Sex", ["male", "female"]) # made some changes to the function here!
job = st.number_input("Job (0-3)", min_value = 0, max_value =3, value =1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate","rich", "quite rich"])
checking_account = st.selectbox("Checking Account", ["little", "moderate","rich"])
credit_amount = st.number_input("Credit Amount", min_value = 0, value = 1000 )
duration = st.number_input("Duration (months)", min_value = 1, value = 12)



input_df = pd.DataFrame({
    "Age" : [age],
    "Sex" : [encoders["Sex"].transform([sex])[0]],
    "Job" : [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
    "Credit amount" : [credit_amount],
    "Duration" : [duration]
}
)

# We 

# Here we are using the same label encoder just like the last one that we used! This will ensure that the right mapping is set based on the last one!
# We are also selecting the first one from the "transform()" results because something like this -> array([2]) is returned! 
'''
This is more about the label encoder
-- fit() learns the mapping from categories to integers.
-- transform() applies that mapping to the data.
-- fit_transform() does both in one step — perfect when you're working with a single dataset and don’t need to reuse the encoder later.
'''


# Then to proceed to creating the prediction button
if st.button("Predict Risk"):
    # Since the Extra Tree model is the one returned, we can use it!

    pred = model.predict(input_df)[0] # This is because an array is returned

    if pred == 1:
        st.success("The predicted credit risk is **GOOD**")
    else:
        st.error("The predicted risk is **BAD**")