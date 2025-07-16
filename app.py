import streamlit as st
import joblib
import pandas as pd

model = joblib.load("voting_model.pkl")
encoder = joblib.load("Encoder.pkl")

st.set_page_config(page_title="Big Mart Sales Predictor")

st.title("📈 Big Mart Sales Prediction")
st.markdown("Enter the product details below to predict the sales.")

Item_Weight = st.number_input("Item Weight", min_value=0.0, value=12.5)
Item_Fat_Content = st.selectbox("Item Fat Content", options=["Low Fat", "Regular"])
Item_Visibility = st.slider("Item Visibility", 0.0, 0.3, 0.1)
Item_Type = st.selectbox("Item Type", options=[
    'Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household',
    'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene',
    'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood'
])
Item_MRP = st.number_input("Item MRP", min_value=0.0, value=150.0)
Outlet_Identifier = st.selectbox("Outlet", options=[
    'OUT049', 'OUT018', 'OUT010', 'OUT013', 'OUT027',
    'OUT045', 'OUT017', 'OUT046', 'OUT035', 'OUT019'
])
Outlet_Establishment_Year = st.selectbox("Outlet Establishment Year", options=[1985, 1987, 1997, 1999, 2002, 2004, 2007, 2009])
Outlet_Size = st.selectbox("Outlet Size", options=['Small', 'Medium', 'High'])
Outlet_Location_Type = st.selectbox("Outlet Location Type", options=['Tier 1', 'Tier 2', 'Tier 3'])
Outlet_Type = st.selectbox("Outlet Type", options=[
    'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store'
])

if st.button("Predict Sales"):
    input_dict = {
        'Item_Weight': [Item_Weight],
        'Item_Fat_Content': [Item_Fat_Content],
        'Item_Visibility': [Item_Visibility],
        'Item_Type': [Item_Type],
        'Item_MRP': [Item_MRP],
        'Outlet_Identifier': [Outlet_Identifier],
        'Outlet_Establishment_Year': [Outlet_Establishment_Year],
        'Outlet_Size': [Outlet_Size],
        'Outlet_Location_Type': [Outlet_Location_Type],
        'Outlet_Type': [Outlet_Type]
    }

    input_df = pd.DataFrame(input_dict)

    for col in input_df.select_dtypes(include='object').columns:
        input_df[col] = encoder.fit_transform(input_df[col])

    prediction = model.predict(input_df)[0]
    st.success(f"🛒 Predicted Sales: ₹{prediction:.2f}")