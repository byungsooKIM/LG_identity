import streamlit as st
import matplotlib.pyplot as plt

st.title("최적 곡률 계산기")
short = st.slider("짧은 변의 길이",0,1000,180)
short = round((short**0.65)/6)*6
st.write("최적의 R 값은", short, "mm 입니다")

# --------------------------------------------------------------------
fig, ax = plt.subplots()

circle_center = (0, 0)    # 원의 중심
circle_radius = short       # 원의 반지름

circle = plt.Circle(circle_center, circle_radius, fc='r', ec='r', fill=True, alpha=0.2)
ax.add_patch(circle)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')

st.pyplot(fig)
