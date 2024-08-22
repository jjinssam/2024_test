import streamlit as st

st.write('Robot Journalism :sunglasses:')
st.title('기사 작성 로봇!!')

name = st.text_input("기자:",  placeholder="작성자 이름")
#food = st.selectbox("좋아하는 음식을 선택하세요:",("")
stadium = st.selectbox("경기장 선택 :", ("","잠실", "고척", "창원", "대구", "광주", "인천", "수원", "사직", "대전") )
winner = st.selectbox("우승팀 선택 :", ("","KIA", "삼성", "LG", "두산", "SSG", "KT", "한화", "롯데", "NC", "키움"))
loser = st.selectbox("진팀 선택 :", ("","KIA", "삼성", "LG", "두산", "SSG", "KT", "한화", "롯데", "NC", "키움"))
mvp = st.text_input("우수선수 :",  placeholder="오늘 경기의 MVP")
score = st.text_input("스코어 :",  placeholder="X:X")

if st.button("위 항목을 선택 후 눌러주세요", type="primary"):
    st.write("=" * 50)
    st.write("오늘",stadium, "에서 야구 경기가 열렸습니다.")
    st.write(winner, "와(과)", loser, "은(는) 치열한 공방전을 펼쳤습니다." )
    st.write(mvp, "이(가) 맹활약을 하였습니다." )
    st.write("결국", winner, "이(가)", loser,"을(를)", score,"로 이겼습니다." )
    st.write("=" * 50)
else:
    st.write("선택 대기중")

#if st.button("입력 초기화", type="primary"):
#    st.session_state.name = ""
#    st.session_state.food = ""
