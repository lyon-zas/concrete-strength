import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('compressive_strength_model.h5')

# Create a function to make predictions with the model
def predict(cement, sand, aggregate, wcr, fib_length, perc_add, wgt_cast, wgt_cure):
  # Create a numpy array with the input values
  x = np.array([[cement, sand, aggregate, wcr, fib_length, perc_add, wgt_cast, wgt_cure]])
  
  # Make a prediction with the model
  y_pred = model.predict(x)[0][0]
  
  # Round the prediction to 2 decimal places
  y_pred = round(y_pred, 2)
  
  # Return the prediction
  return y_pred

# Create a main function
def main():
  # Display a title
  
  st.title('Compressive Strength Prediction')

  
  
  # Create a form to collect input values
  cement = st.number_input('Cement (kg)')
  sand = st.number_input('Sand (kg)')
  aggregate = st.number_input('Aggregate (kg)')
  wcr = st.number_input('Water/Cement Ratio')
  fib_length = st.number_input('Oil Palm Fibre Length (cm)')
  perc_add = st.number_input('Percentage Addition (%)')
  wgt_cast = st.number_input('Weight After Casting (kg)')
  wgt_cure = st.number_input('Weight After Curing (kg)')
  
  # Display a button to trigger the prediction
  if st.button('Predict'):
    # Make a prediction with the model
    comp_strength = predict(cement, sand, aggregate, wcr, fib_length, perc_add, wgt_cast, wgt_cure)
    
    # Display the prediction
    st.write(f'Predicted Compressive Strength: {comp_strength} N/mm²')

# Run the main function
if __name__ == '__main__':
  main()
