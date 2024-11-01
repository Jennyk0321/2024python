import streamlit as st
from datetime import datetime, timedelta
import calendar
import pandas as pd

# 오늘 날짜
today = datetime.today()

# 시작 및 종료 월 설정
start_date = datetime(2024, 12, 1)
end_date = datetime(2025, 11, 30)

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
st.title("📅 2024년 12월부터 1년치 월별 달력 📅")
st.write("아래 달력에서 날짜를 선택하고 일정을 추가해보세요!")

# 달력 표시 및 사용자 인터랙션
selected_date = st.date_input("날짜를 선택해주세요:", today)

# 선택한 날짜에 따라 일정 추가
schedule = st.text_input("일정을 입력하세요:", key="schedule_input")
if st.button("일정 추가"):
    if schedule:
        st.write(f"✅ {selected_date.strftime('%Y-%m-%d')} 일정이 추가되었습니다: {schedule}")
    else:
        st.warning("일정을 입력해 주세요!")

# 달력 표시
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
                
                # 공휴일 표시
                if day_str in holidays:
                    week_columns[i].markdown(f"**{day}** {holidays[day_str]}")
                else:
                    week_columns[i].write(day)
                
                # 오늘 날짜에 커서 표시
                if day_date.date() == today.date():
                    week_columns[i].markdown(f"<div style='background-color: #FFDDC1; padding: 5px; border-radius: 5px;'>📍 오늘</div>", unsafe_allow_html=True)
