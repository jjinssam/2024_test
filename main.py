import streamlit as st

st.write('Hello, *World!* :sunglasses:')
st.title('간단한 인사말 생성기')

title = st.text_input("이름을 입력하세요:", placeholder="한글이름")

st.write('좋아하는 음식을 선택하세요:')
