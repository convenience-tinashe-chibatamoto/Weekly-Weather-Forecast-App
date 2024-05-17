import streamlit as st

st.title("Weekly Weather Forecast: Up to 5 Future days)")
place = st.text_input("Enter any city: ")
days = st.slider("Forecast How Many Days?", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view",
                     ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
