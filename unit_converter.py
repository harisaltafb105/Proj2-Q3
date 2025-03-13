import streamlit as st

# App Title
st.title("🔄 Unit Converter")

# Dropdown options
categories = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Category selection
category = st.selectbox("Select Conversion Category", list(categories.keys()))

# Unit selection with search
unit_from = st.selectbox("Convert From", categories[category])
unit_to = st.selectbox("Convert To", categories[category])

# Input value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Conversion Logic
def convert(value, from_unit, to_unit, category):
    if category == "Length":
        length_factors = {
            "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
            "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371
        }
        return value * (length_factors[to_unit] / length_factors[from_unit])

    elif category == "Weight":
        weight_factors = {
            "Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495
        }
        return value * (weight_factors[from_unit] / weight_factors[to_unit])

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None

# Perform conversion
if st.button("Convert"):
    result = convert(value, unit_from, unit_to, category)
    if result is not None:
        st.success(f"{value} {unit_from} = {result:.2f} {unit_to}")
    else:
        st.error("Conversion not possible.")
