import streamlit as st

# Divide the app into two columns: left for input, right for output
col1, col2 = st.columns(2)

# Left column for inputwith col1:
    st.write('Robot Journalism :sunglasses:')
    st.title('기사 작성 로봇!!')

    name = st.text_input("기자:", placeholder="작성자 이름")
    stadium = st.selectbox("경기장 선택 :", ("", "잠실", "고척", "창원", "대구", "광주", "인천", "수원", "사직", "대전"))
    winner = st.selectbox("우승팀 선택 :", ("", "KIA", "삼성", "LG", "두산", "SSG", "KT", "한화", "롯데", "NC", "키움"))
    loser = st.selectbox("진팀 선택 :", ("", "KIA", "삼성", "LG", "두산", "SSG", "KT", "한화", "롯데", "NC", "키움"))
    mvp = st.text_input("우수선수 :", placeholder="오늘 경기의 MVP")
    score = st.text_input("스코어 :", placeholder="X:X")

# Right column for outputwith col2:
    if st.button("위 항목을 선택 후 눌러주세요", type="primary"):
        st.write("=" * 50)
        st.write(f"오늘 {stadium}에서 야구 경기가 열렸습니다.")
        st.write(f"{winner}와(과) {loser}은(는) 치열한 공방전을 펼쳤습니다.")
        st.write(f"{mvp}이(가) 맹활약을 하였습니다.")
        st.write(f"결국 {winner}이(가) {loser}을(를) {score}로 이겼습니다.")
        st.write("=" * 50)
    else:
        st.write("선택 대기중")
