import streamlit as st
import pandas as pd

# Load the CSV file from the provided GitHub link@st.cachedef load_data():
data = pd.read_csv('population_name.csv')
st.write(data)

# Load the data
#data = load_data()

# Streamlit app
st.title("지역 및 성씨별 인구 데이터 조회")
location = st.selectbox("지역을 선택하세요:",("전국", "서울특별시","부산광역시","대구광역시","인천광역시","광주광역시","대전광역시", "울산광역시","세종특별자치시","경기도","강원도","충청북도","충청남도", "경상남도","경상북도","전라남도","전라북도","제주특별자치도" ))

family_name = st.text_input("성씨를 입력하세요:")

#st.write(location,"의 상위 5개 성씨")

for index in data.iterrows():
    if st.button("검색"):
        if location and family_name:
            # Filter data based on the selected location and entered last name
            filtered_data = data[(data['region'] == location) & (data['surname'] == family_name)]
            
            if not filtered_data.empty:
                population_count = filtered_data.iloc[0]['population']
                fullname_c = filtered_data.iloc[0]['fullname']
                st.write(f"In {location}, there are {population_count} people with the last name {fullname_c}.")
            else:
                st.write(f"No data found for the last name {family_name} in {location}.")
        else:
            st.write("Please select a region and enter a last name.")
    
    #    st.write(location, "Top 5 surnames")
    
    # Display top 5 surnames in the selected regionif location != "nationwide":
    #    top_surnames = data[data['region'] == location].nlargest(5, 'population')[['surname', 'population']]
    #    st.table(top_surnames)
    else:
        st.write("Please select a specific region to see the top 5 surnames.")
