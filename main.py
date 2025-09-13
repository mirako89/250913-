import streamlit as st
import random

st.set_page_config(page_title="MBTI 휴식 추천기", page_icon="😴", layout="centered")

st.title("💡 MBTI 유형별 ✨휴식 추천기✨")
st.write("당신의 MBTI 유형을 선택하면 ✨가장 잘 어울리는 휴식 방법✨을 알려드려요! 🌈")

# MBTI별 휴식 추천 데이터
tips = {
    "INTJ": ["조용히 책 📚 읽기", "미래 계획 세우기 ✍️", "혼자만의 산책 🚶"],
    "ENTP": ["친구들과 수다 💬", "즉흥 여행 ✈️", "보드게임 🎲"],
    "ISFJ": ["집에서 따뜻한 차 ☕ 마시기", "아늑한 영화 감상 🎬", "가족과 저녁 식사 🍲"],
    "ESFP": ["노래방 🎤", "쇼핑 🛍️", "춤추기 💃"],
    "INFJ": ["일기 쓰기 📖", "명상 🧘", "조용한 카페 ☕"],
    "ESTJ": ["운동 🏋️", "집 정리 🧹", "일정 계획 📆"],
    "INFP": ["그림 그리기 🎨", "음악 감상 🎧", "꿈꾸기 🌌"],
    "ENFP": ["친구 만나기 👫", "새로운 취미 배우기 🎸", "파티 🎉"],
    "ISTJ": ["퍼즐 맞추기 🧩", "정리정돈 🪣", "산책 🚶‍♂️"],
    "ESTP": ["스포츠 경기 ⚽", "드라이브 🚗", "모험 🏞️"],
    "ENTJ": ["목표 설정 📊", "자기계발 서적 읽기 📕", "팀 활동 👥"],
    "ISFP": ["그림 감상 🖼️", "자연 산책 🌳", "사진 찍기 📷"],
    "ISTP": ["레고 조립 🧱", "혼자 여행 🌍", "기계 만지작 🔧"],
    "ENFJ": ["봉사활동 🤝", "단체 활동 🎭", "의미 있는 대화 💡"],
    "ESFJ": ["친구 초대 🍽️", "단체 게임 🎮", "쿠키 굽기 🍪"]
}

mbti_types = list(tips.keys())
selected = st.selectbox("👉 당신의 MBTI 유형은 무엇인가요?", ["선택해주세요"] + mbti_types)

if selected != "선택해주세요":
    st.subheader(f"✨ {selected} 유형을 위한 휴식 추천 ✨")
    recommendation = random.choice(tips[selected])
    st.success(f"오늘은 👉 {recommendation} 👈 어떠세요? 🥰")

    # 재미있는 효과 랜덤 실행
    effect = random.choice(["balloons", "snow", "none"])
    if effect == "balloons":
        st.balloons()
    elif effect == "snow":
        st.snow()

    st.markdown("---")
    st.write("💡 *Tip: 가끔은 MBTI와 상관없이 새로운 휴식을 시도해 보는 것도 좋아요!* 🌟")
