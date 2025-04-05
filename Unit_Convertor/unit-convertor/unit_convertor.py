import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer" : 0.001, # 1 m = 0.001 km
        "kilometer_meter" : 1000, # 1 km = 1000 m
        "gram_kilogram" : 0.001,  # 1 gm = 0.001 kgm
        "kilogram_gram" : 1000,  # 1 kgm = 1000 gm
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions :
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not possible"
    
st.title("Unit Convertor")
value = st.number_input("Enter the value:", min_value = 1.0, step = 1.0)

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("To:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value is : {result}")