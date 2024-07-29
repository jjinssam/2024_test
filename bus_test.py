import streamlit as st
import requests
import datetime
import urllib.request

api_key = '7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi/A6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq/J3l6DHA3Q=='

# 올바르게 API 키를 URL에 포함
url = f'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt?ServiceKey={api_key}&busRouteId=100100118&startOrd=1&endOrd=13'

response = requests.get(url)

if response.status_code == 200:
    st.write(response.text)
else:
    st.error(f"API 요청 실패: {response.status_code}")

def get_request_url(url):
    req = urllib.request.Request(url)
    try: #if req:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e: # else :
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# 사용할 API의 Call back URL
end_point = "http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList"
    
# 해당 API가 필요로 하는 파라미터 : 인증키와 검색어
parameters = "?ServiceKey=" + "7LxzdtBw0bYtbx4A4BmxQRkAcrE1pFipyUFEyMi/A6RrxDW7v2eh61RvZYTY29e1WFiL0u9xtucq/J3l6DHA3Q=="
end_point = end_point + parameters + "&strSrch=" + "110" # 110번 버스를 검색하고 싶다
# test
st.write(end_point)
retData = get_request_url(end_point)

st.write(retData)
