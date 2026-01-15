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
plt.rcParams['axes.linewidth'] = 0.2
plt.rc('font', size=4) # 기본 폰트 크기 설정
plt.rc('xtick', labelsize=4) # x축 숫자 크기 설정
plt.rc('ytick', labelsize=4) # y축 숫자 크기 설정
plt.rcParams['xtick.major.width'] = 0.2
plt.rcParams['ytick.major.width'] = 0.2

fig, ax = plt.subplots(figsize=(3,3))

circle_center = (0, 0)    # 원의 중심
circle_radius = short       # 원의 반지름

circle = plt.Circle(circle_center, circle_radius, fc='r', ec='r', fill=True, alpha=0.2)
circle_tv_ui = plt.Circle(circle_center, 60, fc='r', ec='r', fill=False, alpha=1)
circle_fridge_ui = plt.Circle(circle_center, 48, fc='r', ec='r', fill=False, alpha=1)
ax.add_patch(circle)
ax.add_patch(circle_tv_ui)

ax.add_patch(circle_fridge_ui)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_aspect('equal')
plt.grid(True, linewidth=0.2, alpha=0.5, linestyle='--')

st.pyplot(fig)
