import streamlit as st

st.set_page_config(
    page_title="Hello!!!",
    page_icon="👋",
)

st.write("# 欢迎使用 iQVG! 👋")
st.write('# 爱奇艺热点视频信息采集系统')

st.sidebar.success("在上方选择一个演示。")

st.markdown(
    """
    本系统是一个针对爱奇艺设计的用于实时收集热点视频信息的应用系统。
    **👈 从侧边栏选择一个演示**，看看 iQVG 能做什么吧！
    ### 想了解更多吗？
    - 查看 [streamlit.io](https://streamlit.io)了解本系统可视化框架
    - 阅读我的实验报告
    - 或者直接向我提问
    ### 该系统主要功能
    - 使用获取cookie的方式实现自动登陆
    - 使用webdriver获取登录二维码实现预先登录，获取登录用cookie
    - 实现对爱奇艺十个热点视频信息的爬取
    - 实现对热点视频中十个推荐视频信息的爬取
    - 实现对于系统的可视化展示
"""
)
