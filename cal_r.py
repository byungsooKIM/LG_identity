import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

#st.subheader("Optimal Radius Calculator | 最优曲率计算器")
st.markdown("<h6 style='text-align: left; color: #000000;font-size: 20px;'>Optimal Radius Calculator | 最优曲率计算器</h6>", unsafe_allow_html=True)

with st.expander("**계산하는 방법 | 如何计算**", expanded=False):
    st.write("① 짧은 변의 길이에 0.65 제곱한다 | 将较短边的长度乘以 0.65")
    st.write("② 6으로 나누고, 반올림한다 | 除以 6 并向上取整")
    st.write("③ 다시 6을 곱한다 | 再次乘以 6")

input = st.slider("짧은 변의 길이 (㎜) | 短边长 (㎜)",0,1000,180)
short = round((input**0.65)/6)*6
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

circle = plt.Circle(circle_center, circle_radius, fc='r', ec='r', fill=False, alpha=1.0)
#circle_tv_ui = plt.Circle(circle_center, 60, fc='r', ec='black', fill=False, alpha=0.5, linewidth=0.2)
#circle_fridge_ui = plt.Circle(circle_center, 48, fc='r', ec='black', fill=False, alpha=0.5, linewidth=0.2)

calc_value_min = lambda input: (
    6 if input <= 80 else
    18 if input <= 160 else
    30 if input <= 320 else
    42 if input <= 500 else
    54 if input <= 700 else
    72 if input <= 900 else
    84
)
calc_value_max = lambda input: (
    18 if input <= 80 else
    36 if input <= 160 else
    48 if input <= 320 else
    60 if input <= 500 else
    78 if input <= 700 else
    96 if input <= 900 else
    120
)

arc = Wedge(
    center=(0, 0),
    r=calc_value_max(input),                # 바깥 반지름
    theta1=0,          # 시작 각도
    theta2=90,          # 끝 각도
    width=calc_value_max(input)-calc_value_min(input),             # 도넛 두께
    facecolor="#FF0000",
    alpha=0.2
)

ax.add_patch(circle)
#ax.add_patch(circle_tv_ui)
#ax.add_patch(circle_fridge_ui)
ax.add_patch(arc)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_aspect('equal')
plt.grid(True, linewidth=0.2, alpha=0.5, linestyle='--')

st.pyplot(fig)

st.write("허용 범위의 최소값은", calc_value_min(input), "mm, 최대값은", calc_value_max(input), "mm 입니다" )
