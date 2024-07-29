import streamlit as st
import requests
import pandas as pd

# api_key ='7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi%2FA6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq%2FJ3l6DHA3Q%3D%3D'
api_key='7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi/A6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq/J3l6DHA3Q=='
# url = f'﻿http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt?ServiceKey={api_key}&busRouteId=100100118&startOrd=1&endOrd=13'
#  url = f'﻿http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={api_key}'

#test code
url= 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt?ServiceKey=api_key&busRouteId=100100118&startOrd=1&endOrd=13'
# params ={'serviceKey' : api_key, 'busRouteId' : '', 'startOrd' : '1', 'endOrd' : '10' }
# response = requests.get(url, params=params)

response = requests.get(url)
st.write(response.content)
