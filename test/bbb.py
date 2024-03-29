import streamlit as st
import time

# 主页面布局
def main():
    st.title("倒计时器示例")

    # 初始化显示倒计时的空块
    countdown_placeholder = st.empty()

    # 倒计时函数
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            countdown_placeholder.write("倒计时: {}".format(timeformat))
            time.sleep(1)
            t -= 1
        countdown_placeholder.write("倒计时结束！")

    # 设置倒计时时长为10秒
    countdown(10)
    print('================================')
if __name__ == "__main__":
    main()