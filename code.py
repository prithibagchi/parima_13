import pickle
import pandas as pd
import streamlit as st

# Load the saved model
model1 = pickle.load(open('svc_rcv.pkl', 'rb'))

# Load the dataset
df = pd.read_csv("D:\python\Project_2_360dgtmg\DATA\prima_13.csv")

# Specify the title and logo for the web page.
st.set_page_config(
    page_title='Optimization of Unplanned Machine Downtime',
    layout='wide'
)


# Define the app
def app():
    # Add an image and title to the app
    
    st.write("Input Data")
    st.dataframe(df)

    # Create a form to input new data
    st.write("Input New Machine Parameters")
    form = st.form(key='input_form')
    Load_cells = form.slider("Load Cells", min_value=df['Load_cells'].min(), max_value=df['Load_cells'].max(), step=0.5, format="%.3f")
    Hydraulic_Pressure__bar = form.slider("Hydraulic Pressure (bar)", min_value=df['Hydraulic_Pressure__bar'].min(), max_value=df['Hydraulic_Pressure__bar'].max(), step=0.5, format="%.3f")
    Coolant_Pressure__bar = form.slider("Coolant Pressure (bar)", min_value=df['Coolant_Pressure__bar'].min(), max_value=df['Coolant_Pressure__bar'].max(), step=0.5, format="%.3f")
    Air_System_Pressure__bar = form.slider("Air System Pressure (bar)", min_value=df['Air_System_Pressure__bar'].min(), max_value=df['Air_System_Pressure__bar'].max(), step=0.5, format="%.3f")
    Coolant_Temperature__deg_cel = form.slider("Coolant Temperature (deg cel)", min_value=df['Coolant_Temperature__deg_cel'].min(), max_value=df['Coolant_Temperature__deg_cel'].max(), step=0.5, format="%.3f")
    Hydraulic_Oil_Temperature__deg_cel = form.slider("Hydraulic Oil Temperature (deg cel)", min_value=df['Hydraulic_Oil_Temperature__deg_cel'].min(), max_value=df['Hydraulic_Oil_Temperature__deg_cel'].max(), step=0.5, format="%.3f")
    Proximity_sensors = form.slider("Proximity Sensors", min_value=df['Proximity_sensors'].min(), max_value=df['Proximity_sensors'].max(), step=0.5, format="%.3f")
    Spindle_Vibration__microm = form.slider("Spindle Vibration (microm)", min_value=df['Spindle_Vibration__microm'].min(), max_value=df['Spindle_Vibration__microm'].max(), step=0.5, format="%.3f")
    Tool_Vibration__microm = form.slider("Tool Vibration (microm)", min_value=df['Tool_Vibration__microm'].min(), max_value=df['Tool_Vibration__microm'].max(), step=0.5, format="%.3f")
    Spindle_Speed__RPM = form.slider("Spindle Speed (RPM)", min_value=df['Spindle_Speed__RPM'].min(), max_value=df['Spindle_Speed__RPM'].max(), step=0.5, format="%.3f")
    Voltage__volts = form.slider("Voltage (volts)", min_value=df['Voltage__volts'].min(), max_value=df['Voltage__volts'].max(), step=0.5, format="%.3f")
    Torque = form.slider(" Torque", min_value=df[' Torque'].min(), max_value=df[' Torque'].max(), step=0.5, format="%.3f")
    Cutting_Force__kN = form.slider("Cutting_Force__kN", min_value=df['Cutting_Force__kN'].min(), max_value=df['Cutting_Force__kN'].max(), step=0.5, format="%.3f")
    form_submit = form.form_submit_button(label='Submit')

    # Make a prediction with the input data
    if form_submit:
        input_data = [[Load_cells, Hydraulic_Pressure__bar, Coolant_Pressure__bar, Air_System_Pressure__bar,
                       Coolant_Temperature__deg_cel, Hydraulic_Oil_Temperature__deg_cel, Proximity_sensors,
                       Spindle_Vibration__microm, Tool_Vibration__microm, Spindle_Speed__RPM, Voltage__volts, Torque,
                       Cutting_Force__kN]]
        prediction = model.predict(input_data)[0]

        # Display the prediction
        st.write(" Prediction ")
        if prediction == 1:
            st.write("The machine is likely to experience unplanned downtime.")
        else:
            st.write("The machine is likely to experience unplanned downtime.")
            
if __name__ == '__app__':
     app()



