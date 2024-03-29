import streamlit as st
import time
import get_message
import clear_csv
def job():
    with st.spinner("正在获取热播视频信息..."):
        print("当前时间：" + time.strftime("%H:%M:%S"))
        time.sleep(3)
    get_success=st.empty()
    get_success.success('获取信息成功！！！')

st.set_page_config(page_title="Get Video Message", page_icon="🌍")

st.markdown("# 正在热播信息查询")
st.sidebar.header("Get Video Message")

st.write(
    """此页面主要实现热播信息的定时查询"""
)
if st.sidebar.button("缓存数据清除"):
    clear_csv.clear()
    st.sidebar.success('清除成功！！！')
global interval
    
interval_options = [1,5,10,15]
interval = st.selectbox("请选择热点动态更新时间间隔（mins）", interval_options)

st.info(f"当前选择的时间间隔：{interval} mins")
st.write("请点击下方按钮启动定时任务。")
#ccc.ccc()
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        countdown_placeholder.info("倒计时: {}".format(timeformat))
        time.sleep(1)
        t -= 1
    countdown_placeholder.info("倒计时结束！")
if st.button("启动定时任务"):
    while True:
        #job()
        #get_message.get()
        with st.spinner("正在获取热播视频信息..."):
            time.sleep(10)
            st.success('自动登录成功！！！')
            get_success=st.empty()
            get_success.success('获取信息成功！！！')
        countdown_placeholder = st.empty()
        countdown(int(interval)*60)
        #time.sleep(int(interval)*60)




    # 设置倒计时时长为20秒
