import streamlit as st
import pandas as pd

# 主页面布局
def main():
    st.title("展示CSV文件内容")

    # 上传CSV文件
    uploaded_file = st.file_uploader("上传CSV文件", type=['csv'])

    if uploaded_file is not None:
        # 读取上传的CSV文件
        df = pd.read_csv(uploaded_file)
        
        # 展示CSV文件内容
        st.write("### CSV 文件内容：")
        st.dataframe(df,width=1000, height=400)

if __name__ == "__main__":
    main()

    # # 读取 CSV 文件
    df = pd.read_csv("./data/my_dict_data.csv")
    df1 = pd.read_csv("./data/comment/comment1.csv")
    df2 = pd.read_csv("./data/actors/actors1.csv")
    # 选择要展示的行号（假设选择第一行）
    row_number = 0

    # 提取某一行数据
    selected_row = df.iloc[row_number]

    # 展示数据
    st.write("纵向表格:")
    st.dataframe(selected_row,width=800, height=225)
    st.dataframe(df1,width=800, height=400)
    st.dataframe(df2,width=800, height=400)