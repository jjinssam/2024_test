import streamlit as st

st.write('Hello, *World!* :sunglasses:')
st.title('당신의 음식 취향')

title = st.text_input("이름을 입력하세요:", placeholder="한글이름")
option = st.selectbox(
    "좋아하는 음식을 선택하세요:",
    ("망고빙수", "우유빙수", "복숭아빙수", "팥빙수"))

st.button("선택초기화", type="primary")
if st.button("선택 후 눌러주세요"):
    st.write(title,"씨가 좋아하는 음식은",option,"입니다.")
else:
    st.write("선택 대기중")

