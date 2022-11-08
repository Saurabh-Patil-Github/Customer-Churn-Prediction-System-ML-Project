import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def Customer_churn_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The customer is not churn'
    else:
      return 'The customer is churn'
  
    
  
def main():
    
    
    # giving a title
    st.title('Customer Analytics Prediction Web App')
    
    
    # getting the input data from the user
    
    
    tenure = st.text_input('tenure')
    InternetService = st.text_input('InternetService')
    OnlineSecurity = st.text_input('OnlineSecurity')
    TechSupport = st.text_input('TechSupport')
    Contract = st.text_input('Contract')
    PaymentMethod = st.text_input('PaymentMethod')
    
    
    
    # code for Predictionstreamlit run e:/COMPANIES/offcampus/linkedin/Razorpay case study/app.py
    Customer = ''
    
    # creating a button for Prediction
    
    if st.button('Customer Test Result'):
        Customer = Customer_churn_prediction([tenure, InternetService, OnlineSecurity, TechSupport, Contract, PaymentMethod])
        
        
    st.success(Customer)
    
    
    
    
    
if __name__ == '__main__':
    main()