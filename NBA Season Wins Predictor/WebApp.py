import streamlit as st
import joblib
import numpy as np

st.title('NBA Team Wins Predictor')

st.text("Through this project, these 5 metrics helped best estimate an NBA team's season wins")

#Retreiving Data Needed from Notebook
model = joblib.load('NBA Season Wins Predictor\model.pkl')
means = np.array([0.01666667, 0.02      , 0.4997    , 0.5524    , 0.27556667]) #Need scaled means to standardize user inputs, retrieved using scaler.mean_ in the notebook
StDev = np.array([4.37996068, 4.20050791, 0.02702733, 0.01791945, 0.02473686]) #Standard Deviations retrieved from scaler.scale_, needed as well to standardize user inputs


#Creating Sliders for Users to toggle and test different metric combinations
E_NET = st.slider('Estimated NET Rating (luck adjusted rating using advanced metrics)', min_value=-15.0, max_value=15.0, step = .1)
#In dataset used and using pandas, minmum found for a team was -10.5 and max was 11.2

NET = st.slider('NET Rating', min_value=-15.0, max_value=15.0,step = .1) #Minimum found was -10.6, max was 11.7

PIE = st.slider('Team PIE (Player Impact Estimate)',min_value=.35, max_value=.6) #Minimum found was .434, max was .555

TS_PCT = st.slider('Team True Shooting PCT',min_value=.45, max_value=.7) #Minimum found was .529 and max was .609

OFF_REB = st.slider('Team Offensive Rebound PCT', min_value=.15,max_value=.40) #Minimum found  was .224 and max was .344

inputs = np.array([E_NET,NET,PIE,TS_PCT,OFF_REB])


# Standardized value = (given value - mean)/(standard deviation of feature)
def standardize(user_inputs):
    return (user_inputs - means)/StDev

standardized_inputs = standardize(inputs)

st.text(model.predict(standardized_inputs.reshape(1,-1)))