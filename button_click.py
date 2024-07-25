import streamlit as st

cnt = 0
if st.button('버튼버튼버튼!!!',key=0): 
  cnt += 1
st.write(f'### 누른 횟수는 :green[{cnt}] 입니다.')
