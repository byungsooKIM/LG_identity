import streamlit as st
import matplotlib.pyplot as plt

st.title("Optimal Radius Calculator")

with st.expander(":material/priority_high: **계산하는 방법 | 如何计算**", expanded=False):
    st.write("① 짧은 변의 길이에 0.65 제곱한다 | 将较短边的长度乘以 0.65")
    st.write("② 6으로 나누고, 반올림한다 | 除以 6 并向上取整")
    st.write("③ 다시 6을 곱한다 | 再次乘以 6")

short = st.slider("짧은 변의 길이 | 短边长",0,1000,180)
short = round((short**0.65)/6)*6
st.write("최적의 R 값은", short, "mm 입니다")

# --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(3,3))

circle_center = (0, 0)    # 원의 중심
circle_radius = short       # 원의 반지름

circle = plt.Circle(circle_center, circle_radius, fc='r', ec='r', fill=True, alpha=0.2)
ax.add_patch(circle)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')

st.pyplot(fig)
