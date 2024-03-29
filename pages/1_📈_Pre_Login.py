import streamlit as st

import login
st.set_page_config(page_title="自动登录", page_icon="📈")

st.markdown("# 自动登录")
st.sidebar.header("自动登录")
st.write(
    """这个页面主要实现iqiyi的预先登录用以获得cookie，以便于后续自动登录。希望你喜欢！"""
)

if st.button('获取登录二维码'):
    
    #st.write('正在获取登录二维码...')
    login.prelogin()
