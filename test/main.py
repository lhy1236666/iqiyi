import streamlit as st
import time
import schedule
import subprocess
import login


#my_function()


def run_scheduled_task():
    subprocess.Popen(["python", "get_message.py"])

def job():
    st.write(f"这个函数每隔{interval}秒执行一次！当前时间：" + time.strftime("%H:%M:%S"))

# 利用schedule库设置每5秒执行一次job函数
def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Streamlit应用的界面布局
def main():
    global interval
    
    interval_options = [5, 8, 10]
    interval = st.selectbox("请选择定时执行的时间间隔（秒）", interval_options)

    st.write(f"当前选择的时间间隔：{interval}秒")
    st.write("请点击下方按钮启动定时任务。")

    if st.button("启动定时任务"):
        schedule.clear()
        schedule.every(int(interval)).seconds.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)
        #threading.Thread(target=start_scheduler, daemon=True).start()
    if st.button('终止任务'):
        schedule.clear()



def run_scheduled_task():
    print("当前时间：" + time.strftime("%H:%M:%S"))
    subprocess.Popen(["python", "ccc.py"])
    print("当前时间：" + time.strftime("%H:%M:%S"))
def job():
    print("当前时间：" + time.strftime("%H:%M:%S"))
    time.sleep(3)

# 启动Streamlit应用及定时器
if __name__ == '__main__':
    # 创建一个新线程用于执行定时器
    #threading.Thread(target=start_scheduler, daemon=True).start()
    # 添加侧边栏
    st.sidebar.title('侧边栏标题')

    # 在主界面添加内容
    st.title('爱奇艺热点视频信息采集')
    # 添加一个文本输入框
    
    st.subheader('自动登录')

    if st.button('获取登录二维码'):
        
        #st.write('正在获取登录二维码...')
        login.prelogin()

    # 添加一个滑动条
    #slider_input = st.slider('选择一个值', 0, 100, 50)

    # 添加一个按钮

    #运行Streamlit应用
    main()

    