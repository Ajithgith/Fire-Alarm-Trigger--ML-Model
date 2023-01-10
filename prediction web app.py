# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:37 2022

@author: ajith
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/ajith\Downloads/Trained Model/trained_model.sav', 'rb'))

#Creating a function for prediction

def fire_detection(input_data):
    
    #changing input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshaping the array as we are predicting only for one instance

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
        
    if(prediction[0] == 1):
        return "Fire is there"
    else:
        return "Fire is not there"
    
    
def main():
    
    
    #giving a title     
    st.title("Fire Detection")
    
    
    #getting the input data from the user
    
    Index = st.text_input('Index')
    UTC = st.text_input('UTC')
    Temperature = st.text_input('Temperature[C]')
    Humidity = st.text_input('Humidity[%]')
    TVOC = st.text_input('TVOC[ppb]')
    eCO2 = st.text_input('eCO2[ppm]')
    Raw_H2 = st.text_input('Raw H2')
    Raw_Ethanol = st.text_input('Raw Ethanol')
    Pressure = st.text_input('Pressure[hPa]')
    PM1 = st.text_input('PM1.0')
    PM2 = st.text_input('PM2.5')
    NC0 = st.text_input('NC0.5')
    NC1 = st.text_input('NC1.0')
    NC2 = st.text_input('NC2.5')
    CNT = st.text_input('CNT')
    
    
    #code for prediction
    
    smoke = ''
    
    #creating a button for prediction
    
    if st.button("Fire Test Result"):
        smoke = fire_detection([Index, UTC, Temperature, Humidity, TVOC, eCO2, Raw_H2, Raw_Ethanol, Pressure, PM1, PM2, NC0, NC1, NC2, CNT])

    
    st.success(smoke)
        

    
    
    
    
    
    

