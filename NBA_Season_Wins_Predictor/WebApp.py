import streamlit as st
import joblib
import numpy as np

st.title('NBA Team Wins Predictor')

st.text("Through this project, these 5 metrics helped best estimate an NBA team's season wins")

#Retreiving Data Needed from Notebook
model = joblib.load('NBA_Season_Wins_Predictor/model.pkl')
means = np.array([0.01666667, 0.02      , 0.4997    , 0.5524]) #Need scaled means to standardize user inputs, retrieved using scaler.mean_ in the notebook
StDev = np.array([4.37996068, 4.20050791, 0.02702733, 0.01791945]) #Standard Deviations retrieved from scaler.scale_, needed as well to standardize user inputs


#Creating Sliders for Users to toggle and test different metric combinations

left, right = st.columns(2, gap='large')
with left:
    NET = st.slider('NET Rating', min_value=float(-15.0), max_value=float(15.0),step = .1,value=float(means[1])) #Minimum found was -10.6, max was 11.7
    E_NET = st.slider('Estimated NET Rating (luck adjusted rating using advanced metrics)', min_value=float(-15.0), max_value=float(15.0), step = .1,value=float(means[0]))#Minmum found for a team was -10.5 and max was 11.2

with right:
    PIE = st.slider('Team PIE (Player Impact Estimate)',min_value=float(.35), max_value=float(.6),value=float(means[2])) #Minimum found was .434, max was .555

    TS_PCT = st.slider('Team True Shooting PCT',min_value=float(.45), max_value=float(.7),value=float(means[3])) #Minimum found was .529 and max was .609



st.text('Normally the Estimated NET Rating value is similar to normal NET rating, \nso for this model to work well the values for both should be in a similar \nrange to each other')
inputs = np.array([E_NET,NET,PIE,TS_PCT])


# Standardized value = (given value - mean)/(standard deviation of feature)
def standardize(user_inputs):
    return (user_inputs - means)/StDev

standardized_inputs = standardize(inputs)

st.header("Estimated Wins", divider='gray')

st.subheader(round(float(model.predict(standardized_inputs.reshape(1,-1))), 4))