import streamlit as st

if "cnt" not in st.session_state: 
  st.session_state.cnt=0
if st.button('버튼버튼버튼!!!',key=0): 
  st.session_state.cnt += 1
st.write(f'### 누른 횟수는 :green[{st.session_state.cnt}] 입니다.')
