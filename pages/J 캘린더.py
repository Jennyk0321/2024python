import streamlit as st
from datetime import datetime, timedelta
import calendar
import pandas as pd

# 오늘 날짜
today = datetime.today()

# 시작 및 종료 월 설정
start_date = datetime(2024, 11, 1)
end_date = datetime(2025, 12, 31)

# 달력 생성을 위한 날짜 범위 생성
dates = pd.date_range(start=start_date, end=end_date, freq='MS')

# 공휴일 설정 (임의로 주요 공휴일 표시)
holidays = {
    '2024-12-25': '🎄 크리스마스',
    '2025-01-01': '🎉 새해 첫날',
    '2025-02-10': '🌸 설날',
    '2025-02-11': '🌸 설날',
    '2025-03-01': '🇰🇷 삼일절',
    '2025-05-05': '🎏 어린이날',
    '2025-06-06': '🇰🇷 현충일',
    '2025-08-15': '🇰🇷 광복절',
    '2025-09-14': '🌕 추석',
    '2025-09-15': '🌕 추석',
    '2025-10-03': '🇰🇷 개천절',
    '2025-10-09': '🇰🇷 한글날',
    '2025-12-25': '🎄 크리스마스'
}

# Streamlit 레이아웃
st.title("📅 2024년 11월부터 2025년 12월까지 월별 달력 📅")
st.write("아래 달력에서 날짜를 더블클릭하여 일정을 추가해보세요!")

# 선택된 날짜 및 시간과 일정 저장을 위한 상태 초기화
if "schedule_data" not in st.session_state:
    st.session_state["schedule_data"] = {}

# 일정 추가 인터페이스 (더블클릭으로 일정 입력)
selected_date = st.date_input("날짜를 선택하고 일정을 더블클릭하여 입력하세요:", today)

if selected_date:
    date_key = selected_date.strftime("%Y-%m-%d")
    
    # 사용자 입력: 시간과 일정
    with st.expander(f"{date_key} 일정 등록", expanded=True):
        selected_time = st.time_input("시간을 선택해주세요:", datetime.now().time())
        schedule = st.text_input("일정을 입력하세요:")
        details = st.text_area("세부 메모 작성")

        if st.button("일정 등록"):
            if schedule:
                # 일정 저장
                if date_key not in st.session_state["schedule_data"]:
                    st.session_state["schedule_data"][date_key] = []

                st.session_state["schedule_data"][date_key].append({
                    "time": selected_time.strftime("%H:%M"),
                    "event": schedule,
                    "details": details
                })
                st.
