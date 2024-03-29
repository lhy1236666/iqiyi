import streamlit as st
import pandas as pd
import get_revideo
import random
import numpy as np
st.set_page_config(page_title="Message Show", page_icon="📊")

st.markdown("# 信息展示")
st.sidebar.header("Message Show")
st.write(
    """本页面用于展示抓取的热点视频以及对应热点关联影片信息"""
)
#st.sidebar.checkbox('qqqq', True)
type_options=['热点视频','猜你喜欢']
type=st.sidebar.selectbox("热点视频 or 猜你喜欢", type_options)
if type=='热点视频':
    interval_options = [1,2,3,4,5,6,7,8,9,10]
    interval = st.sidebar.selectbox("请选择您要查询的影片id", interval_options)
    # # 读取 CSV 文件
    df = pd.read_csv("./data/my_dict_data.csv")
    df1 = pd.read_csv("./data/comment/comment"+str(interval)+".csv")
    df2 = pd.read_csv("./data/actors/actors"+str(interval)+".csv")
    # # 选择要展示的行号（假设选择第一行）
    # row_number = interval-1

    # # 提取某一行数据
    # selected_row = df.iloc[row_number]
    intorduction = df[df['id'] == interval]['introdution'].values[0]
    name1 = df[df['id'] == interval]['name'].values[0]
    hot_num = df[df['id'] == interval]['hot_num'].values[0]
    url= df[df['id'] == interval]['url'].values[0]
    # 展示数据
    st.subheader("视频简要信息:")
    name=st.container(height=150,border=True)
    name.markdown('<font size=5  face="黑体">'+ '**'+name1+'**' +'</font>' , unsafe_allow_html=True)
    name.markdown('<font size=3  face="宋体"> **id='+ str(interval)+ ' 视频热度：'+str(hot_num) + '** </font>' ,unsafe_allow_html=True)
    name.markdown('[点击此处跳转]('+url+')') 
    st.subheader("视频简介:")
    intro=st.container(height=200,border=True)
    try:
        intro.markdown('<font face="宋体"  size=4> '+intorduction+' </font>', unsafe_allow_html=True)
    except:
        intro.markdown('<font face="宋体"  size=4> 暂无简介 </font>', unsafe_allow_html=True)
    # st.subheader("视频简要信息:")
    # st.dataframe(selected_row,width=800, height=225)
    uname_list = df1['uname'].values
    a=len(uname_list)
    st.subheader("热点评论信息:")
    for num in range(a):
        usr_name=df1.iloc[num]['uname']
        content=df1.iloc[num]['content']
        time=df1.iloc[num]['addtime']
        likes=df1.iloc[num]['likes']
        uid=df1.iloc[num]['uid']
        words = ["user", "assistant",  "human","ai"]
        selected_word=words[num%4]
        with st.chat_message(selected_word):
            st.write(usr_name+" :")
            st.markdown('<font face="宋体"  size=4> '+content+' </font>', unsafe_allow_html=True)
            st.write(time+"  :rose:"+str(likes)+'  [uid:](https://www.iqiyi.com/paopao/u/'+str(uid)+'/)'+str(uid))
        
    st.subheader("演职人员表:")
    st.dataframe(df2,width=800, height=400)
else:

    # 读取 CSV 文件
    df = pd.read_csv('./data/my_dict_data.csv')

    # 提取指定列的数据
    column_data = df['name'].values  # 将 'ColumnName' 替换为你要提取的列名

    interval_options = column_data
    interval = st.sidebar.selectbox("请选择您要获取哪一热点视频的前十条推荐视频信息：", interval_options)
    url = df[df['name'] == interval]['url'].values[0]
    flag=st.sidebar.checkbox('显示推荐视频信息',False)
    if st.sidebar.button('一键获取'):
        with st.spinner("正在获取推荐视频信息..."):
            get_revideo.get_veideo(url)
        st.success('获取信息成功！！！')

    if flag:
        dfre = pd.read_csv("./data/redata/revideo_data.csv")
        name_data = dfre['name'].values
        
        reid_options = name_data
        rename = st.selectbox("请选择您要查询的推荐影片的信息：", reid_options)
        reid=dfre[dfre['name'] == rename]['id'].values[0]

        intorduction = dfre[dfre['name'] == rename]['introdution'].values[0]
        name1 = dfre[dfre['name'] == rename]['name'].values[0]
        hot_num = dfre[dfre['name'] == rename]['hot_num'].values[0]
        url= dfre[dfre['name'] == rename]['url'].values[0]
        # 展示数据
        st.subheader("视频简要信息:")
        name=st.container(height=150,border=True)
        name.markdown('<font size=5  face="黑体">'+ '**'+name1+'**' +'</font>' , unsafe_allow_html=True)
        name.markdown('<font size=3  face="宋体"> **id='+ str(reid)+ ' 视频热度：'+str(hot_num) + '** </font>' ,unsafe_allow_html=True)
        name.markdown('[点击此处跳转]('+url+')') 
        st.subheader("视频简介:")
        intro=st.container(height=200,border=True)
        try:
            intro.markdown('<font face="宋体"  size=4> '+intorduction+' </font>', unsafe_allow_html=True)
        except:
            intro.markdown('<font face="宋体"  size=4> 暂无简介 </font>', unsafe_allow_html=True)


        #st.subheader("推荐视频信息:")
        #st.dataframe(dfre,width=800, height=400)
        df1 = pd.read_csv("./data/redata/comment/comment"+str(reid)+".csv")
        df2 = pd.read_csv("./data/redata/actors/actors"+str(reid)+".csv")
        uname_list = df1['uname'].values
        a=len(uname_list)
        st.subheader("热点评论信息:")
        for num in range(a):
            usr_name=df1.iloc[num]['uname']
            content=df1.iloc[num]['content']
            time=df1.iloc[num]['addtime']
            likes=df1.iloc[num]['likes']
            uid=df1.iloc[num]['uid']
            words = ["user", "assistant",  "human","ai"]
            selected_word=words[num%4]
            with st.chat_message(selected_word):
                st.write(usr_name+" :")
                st.markdown('<font face="宋体"  size=4> '+content+' </font>', unsafe_allow_html=True)
                st.write(time+"  :rose:"+str(likes)+'  [uid:](https://www.iqiyi.com/paopao/u/'+str(uid)+'/)'+str(uid))
        st.subheader("演职人员表:")
        st.dataframe(df2,width=800, height=400)