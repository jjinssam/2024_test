import streamlit as st

st.write('Hello, *World!* :sunglasses:')
st.title('간단한 인사말 생성기')

title = st.text_input("이름을 입력하세요:", placeholder="한글이름")
option = st.selectbox(
    "좋아하는 음식을 선택하세요:",
    ("망고빙수", "우유빙수", "복숭아빙수", "팥빙수"))

st.write(title,"씨가 좋아하는 음식은",option,"입니다.")
