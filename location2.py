import streamlit as st
import pandas as pd

# Load the CSV file 
data = pd.read_csv('population_name.csv')

# Streamlit app
st.title("지역 및 성씨별 인구 데이터 조회")

location = st.selectbox(
    "지역을 선택하세요:",
    ("전국", "서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시", "대전광역시", "울산광역시", 
     "세종특별자치시", "경기도", "강원도", "충청북도", "충청남도", "경상남도", "경상북도", "전라남도", "전라북도", "제주특별자치도")
)

family_name = st.text_input("성씨를 입력하세요:")

# Search buttonif st.button("검색"):
    # Filter data based on the selected location and entered last name
if st.button("검색"):
    filtered_data = data[(data['region'] == location) & (data['surname'] == family_name)]
    filtered_data_new = filtered_data.drop(filtered_data.columns[0], axis=1)
    if not filtered_data.empty:
        st.write(f"{location}에서 '{family_name}'씨 인구 수:")
        st.table(filtered_data_new)
    else:
        st.write(f"{location}에서 '{family_name}' 씨를 가진 데이터를 찾을 수 없습니다.")
else:
    st.write("지역과 성씨를 입력하고 '검색' 버튼을 눌러주세요.")
