import streamlit as st
import requests
import pandas as pd

# api_key ='7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi%2FA6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq%2FJ3l6DHA3Q%3D%3D'
  api_key='7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi/A6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq/J3l6DHA3Q=='
# url = f'﻿http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt?ServiceKey={api_key}&busRouteId=100100118&startOrd=1&endOrd=13'
  url = f'﻿http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={api_key}'
#test code
url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt'
params ={'serviceKey' : api_key, 'busRouteId' : '', 'startOrd' : '1', 'endOrd' : '10' }

response = requests.get(url, params=params)
st.write(response.content)

# Function to fetch real-time bus data
def get_bus_data():
    st.write(url)
    response = requests.get(url)
    st.write(response)  #추가
    
    if response.status_code == 200:
        data = response.json()
        # Process the data to a pandas DataFrame if necessary
        bus_data = pd.DataFrame(data['busInfo'])  # Adjust based on the actual structure of the API response
        return bus_data
    else:
        st.error("Failed to fetch bus data")
        return None

# Streamlit app
st.title("Real-time Bus Location")

# Fetch bus data
bus_data = get_bus_data()

# Display bus data
if bus_data is not None:
    st.write("Real-time Bus Locations")
    st.table(bus_data)
else:
    st.write("No data available at the moment.")
