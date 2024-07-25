import streamlit as st

st.write('Hello, *World!* :sunglasses:')
st.title('당신의 음식 취향')

name = st.text_input("이름을 입력하세요:", placeholder="한글이름")
food = st.selectbox("좋아하는 음식을 선택하세요:",("","망고빙수", "우유빙수", "복숭아빙수", "팥빙수"))

if st.button("선택 후 눌러주세요", type="primary"):
    st.write(name,"씨가 좋아하는 음식은",food,"입니다.")
else:
    st.write("선택 대기중")

if st.button("입력 초기화", type="primary"):
    st.session_state.name = ""
    st.session_state.food = ""

