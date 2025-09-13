import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("🌍 MBTI 유형별 국가 비율 Top 10")

# 기본 파일 경로
file_path = "countriesMBTI_16types.csv"

# 파일 불러오기 (폴더에 없으면 업로드 기능 사용)
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()  # 파일 없으면 실행 중단

# MBTI 유형 선택 박스
mbti_types = [col for col in df.columns if col != "Country"]
selected_mbti = st.selectbox("MBTI 유형을 선택하세요:", mbti_types)

# 선택된 MBTI 기준 상위 10개국 추출
top10 = df[["Country", selected_mbti]].nlargest(10, selected_mbti)

# Altair 차트
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_mbti, title="비율", scale=alt.Scale(domain=[0, top10[selected_mbti].max()*1.1])),
        y=alt.Y("Country", sort="-x"),
        tooltip=["Country", selected_mbti]
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
