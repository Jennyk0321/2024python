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
                st.success(f"{date_key} 일정이 추가되었습니다: {schedule}")
            else:
                st.warning("일정을 입력해 주세요!")

# 달력 표시 및 일정 출력
for date in dates:
    month = date.month
    year = date.year

    st.subheader(f"{year}년 {month}월")

    # 해당 월의 달력 생성
    cal = calendar.monthcalendar(year, month)
    columns = st.columns(7)

    # 요일 헤더
    for i, day in enumerate(['월', '화', '수', '목', '금', '토', '일']):
        columns[i].write(f"**{day}**")

    # 주별 날짜 표시
    for week in cal:
        week_columns = st.columns(7)
        for i, day in enumerate(week):
            if day == 0:
                week_columns[i].write(" ")
            else:
                day_date = datetime(year, month, day)
                day_str = day_date.strftime("%Y-%m-%d")

                # 공휴일 또는 주말 표시
                day_text = f"**{day}**"
                if day_str in holidays:
                    # 공휴일 빨간색 표시
                    week_columns[i].markdown(f"<span style='color: red;'>{day_text} {holidays[day_str]}</span>", unsafe_allow_html=True)
                elif i == 5:  # 토요일
                    week_columns[i].markdown(f"<span style='color: red;'>{day_text}</span>", unsafe_allow_html=True)
                elif i == 6:  # 일요일
                    week_columns[i].markdown(f"<span style='color: red;'>{day_text}</span>", unsafe_allow_html=True)
                else:
                    week_columns[i].write(day_text)

                # 일정 표시
                if day_str in st.session_state["schedule_data"]:
                    for event in st.session_state["schedule_data"][day_str]:
                        week_columns[i].write(f"🕒 {event['time']} - {event['event']}")

                # 오늘 날짜에 커서 표시
                if day_date.date() == today.date():
                    week_columns[i].markdown(f"<div style='background-color: #FFDDC1; padding: 5px; border-radius: 5px;'>📍 오늘</div>", unsafe_allow_html=True)
