import streamlit as st
import requests

api_key = '7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi/A6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq/J3l6DHA3Q=='

# 올바르게 API 키를 URL에 포함
url = f'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt?ServiceKey={api_key}&busRouteId=100100118&startOrd=1&endOrd=13'

response = requests.get(url)

if response.status_code == 200:
    st.write(response.text)
else:
    st.error(f"API 요청 실패: {response.status_code}")
