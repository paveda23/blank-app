import streamlit as st
import pandas as pd
import plotly.express as px

# 샘플 데이터프레임 생성 (국가, 남성 인구, 여성 인구)
data = {
    'Country': ['USA', 'China', 'India', 'Brazil', 'Russia', 'South Korea', 'Germany', 'France'],
    'Male': [160, 700, 700, 100, 70, 25, 40, 32],
    'Female': [165, 670, 680, 105, 80, 26, 42, 34]
}

df = pd.DataFrame(data)
df['Ratio'] = df['Male'] / df['Female']

# Streamlit 애플리케이션 설정
st.title("세계 남녀 비율 시각화")

# 검색 기능 추가
country = st.selectbox("국가를 선택하세요:", df['Country'])
selected_data = df[df['Country'] == country]

if not selected_data.empty:
    st.write(f"{country}의 남녀 비율:")
    st.write(f"남성: {selected_data['Male'].values[0]}, 여성: {selected_data['Female'].values[0]}")
    st.write(f"비율 (남성:여성): {selected_data['Ratio'].values[0]:.2f}")

# 전체 국가의 남녀 비율을 지도로 시각화
fig = px.choropleth(df,
                    locations="Country",
                    locationmode='country names',
                    color="Ratio",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="세계 남녀 비율 지도",
                    labels={'Ratio': '비율 (남성:여성)'})

st.plotly_chart(fig)
