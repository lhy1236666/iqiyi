import streamlit as st
import requests
from PIL import Image

# 主页面布局
def main():


    # 读取本地图片文件
    image_path = "login.jpg"  # 修改为你的本地图片路径
    image = Image.open(image_path)

    # 显示图片
    st.write("展示本地图片：")
    st.image(image, caption="本地图片", width=150)

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     #main()
#         # 设置图片 URL
#     image_url = "https://qrcode.iqiyipic.com/login/?data=https%3A%2F%2Fpassport.iqiyi.com%2Fapis%2Fqrcode%2Ftoken_login.action%3Ftoken%3D7a068e2289029a0273bcf76251df36dca&property=0&salt=7a91bc61256370f6859a71aea3577b7e&width=162&_=0.6931041630633925"

#     # 发送 HTTP 请求获取图片数据
#     response = requests.get(image_url)

#     # 检查请求是否成功
#     if response.status_code == 200:
#         # 指定本地保存路径和文件名
#         local_file_path = "111.jpg"

#         # 写入图片数据到本地文件
#         with open(local_file_path, "wb") as file:
#             file.write(response.content)
        
#         print("图片下载成功，保存路径为:", local_file_path)
#     else:
#         print("图片下载失败")