import streamlit as st

st.set_page_config(
    initial_sidebar_state="collapsed",layout= "wide", page_icon="😊",
    page_title="나만의 스트림릿"
)

with st.sidebar :
    st.write("안녕~ 사이드바")
    st.write("닫을수도 있습니다.")

st.write("이건 메인 페이지에 있는 텍스트")