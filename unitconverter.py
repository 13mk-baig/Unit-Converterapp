import streamlit as st


 #Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color:#9F79B8; /* Light lilac */
        }
        
        h1 {
            text-align: center;
            color: #6a1b9a;
        }
        .stSelectbox, .stNumberInput {
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(255, 105, 180, 0.2); /* Pinkish shadow */
            margin-bottom: 20px;
        }
        label, .stTextInput label, .stSelectbox label, .stNumberInput label {
            display: block;
            text-align: center;
            font-weight: bold;
            margin-bottom: 8px;
            color: #6a1b9a;
        }
        .stButton>button {
            background-color: #ff69b4;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            margin-top: 20px;
        }
        .stButton>button:hover {
            background-color: #ff85c1;
        }
        .stSuccess {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Wrapper box
st.markdown('<div class="container">', unsafe_allow_html=True)



#functionality
def distance_convertor(from_unit,to_unit,value):
    units ={
        "meters":1,
        "kilometers":1000,
        "feet":0.3048,
        "miles":1609.34,
    }
    result = value*units[from_unit]/ units[to_unit]
    return result

def temperature_convertor(from_unit,to_unit,value):
    if from_unit== "celcius" and  to_unit =="fahrenheit":
        result=(value*9/5) +32
    elif from_unit=="fahrenheit"and to_unit =="celcius":
        result=(value -32 )*5/9
    else:
        result=value
    return result

def weight_convertor(from_unit,to_unit,value):
    units ={
        "kilograms":1,
        "grams":0.001,
        "pounds":0.453592,
        "ounces":0.0283495,
    }
    result = value*units[from_unit]/ units[to_unit]
    return result
def pressure_convertor(from_unit,to_unit,value):
    units ={
        "pascals":1,
        "hectopascals":100,
        "kilopascals":1000,
        "bar":100000,
    }
    result = value*units[from_unit]/ units[to_unit]
    return result
def length_convertor(from_unit,to_unit,value):
    units ={
        "kilometer": 1000,
    "meter": 1,
    "centimeter": 0.01,
    "millimeter": 0.001,
    }
    result = value*units[from_unit]/ units[to_unit]
    return result
def time_convertor(from_unit,to_unit,value):
    units ={
    "minutes": 60,
    "seconds": 1,
    "hours": 3600,            # 60 minutes * 60 seconds
    "days": 86400,            # 24 hours * 3600 seconds
    "weeks": 604800,          # 7 days * 86400 seconds
    "months": 2629746,  
    }
    result = value*units[from_unit]/ units[to_unit]
    return result



# user interface 
st.title("🌐 Unit Converter App")
category =st.selectbox("select category",["distance","temperature","weight","length","time","pressure"])
if category == "distance":
    from_unit=st.selectbox("from",["meters","kilometers","feet","miles"])
    to_unit=st.selectbox("to",["meters","kilometers","feet","miles"])
    value=st.number_input("enter value ")
    if st.button("convert"):
        result=distance_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit}={result: .2f}{to_unit}")

elif category == "temperature":  
    from_unit=st.selectbox("from",["celcius","fahrenheit"])
    to_unit=st.selectbox("to",["celcius","fahrenheit"])
    value=st.number_input("enter value ")
    if st.button("convert"):
        result=temperature_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit}={result: .2f}{to_unit}")

elif category == "weight":  
    from_unit=st.selectbox("from",["kilograms","grams","pounds","ounces"])
    to_unit=st.selectbox("to",["kilograms","grams","pounds","ounces"])
    value=st.number_input("enter value ")
    if st.button("convert"):
        result=weight_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit}={result: .2f}{to_unit}")


elif category == "pressure":  
    from_unit=st.selectbox("from",["pascals","hectopascals","kilopascals","bar"])
    to_unit=st.selectbox("to",["pascals","hectopascals","kilopascals","bar"])
    value=st.number_input("enter value ")
    if st.button("convert"):
        result=pressure_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit}={result: .2f}{to_unit}")

elif category == "length":  
    from_unit=st.selectbox("from",["kilometer","meter","centimeter","millimeter"])
    to_unit=st.selectbox("to",["kilometer","meter","centimeter","millimeter"])
    value=st.number_input("enter value ")
    if st.button("convert"):
        result=length_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit}={result: .2f}{to_unit}") 
          
elif category == "time":  
    from_unit=st.selectbox("from",["minutes","seconds","hours","days","weeks","months"])
    to_unit=st.selectbox("to",["minutes","seconds","hours","days","weeks","months"])
    value=st.number_input("enter value ")
    if st.button("convert"):
        result=time_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit}={result: .2f}{to_unit}") 
        # Close wrapper div
st.markdown("</div>", unsafe_allow_html=True) 