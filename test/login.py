from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re
import requests
import streamlit as st
from PIL import Image

def prelogin():
    # 1. 创建浏览器打开需要自动登录的网页
    with st.spinner("正在获取登录二维码..."):
        option=Options()
        option.add_argument('--headless')
        option.add_argument("--window-size=1960,1080")
        driver = webdriver.Chrome(options = option)
        driver.get('https://www.iqiyi.com/')
        driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/img').click()

        driver.find_element(By.CSS_SELECTOR,'#J-user-icon').click()
        time.sleep(1)

        driver.find_element(By.XPATH,'/html/body/div[5]/div/div[1]/div[3]/div[2]/div/div/div/div[5]/div[1]/a[1]').click()
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        url=soup.find_all('div',class_='qrcode-pic')
        #url=driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(18) > div > div.qy-login-container > div.qy-login-container-right > div.qy-login-main > div > div > div > div:nth-child(2) > div.qy-login-qrcode > div.qrcode-pic > img').get_attribute('src')
        url = re.search(r'src="([^"]+)', str(url))
        print(url.group(1))
        response = requests.get('https:'+url.group(1))
        if response.status_code == 200:
            # 指定本地保存路径和文件名
            local_file_path = "login.jpg"

            # 写入图片数据到本地文件
            with open(local_file_path, "wb") as file:
                file.write(response.content)
            image_path = "login.jpg"  # 修改为你的本地图片路径
            image = Image.open(image_path)

            # 显示图片
            st.success("二维码获取成功！！！")
            st.image(image, caption="登录二维码", width=250)
        else:
            st.exception("图片下载失败")
    # 2. 留足够长的时间给人工完成登录
    # （完成登录的时候必须保证浏览器对象指向的窗口能够看到登录成功的效果）

    # 进入网页后会有登录提示，手动扫码登录成功后，回到pycharm的输出区输入任意
    # 字符给input，方便我们知道执行到什么地方了
    # 3. 获取浏览器cookie保存到本地文件        
    
    st.info("请在20秒内扫码登录........")
    countdown_placeholder = st.empty()

    # 倒计时函数
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            countdown_placeholder.info("倒计时: {}".format(timeformat))
            time.sleep(1)
            t -= 1
        countdown_placeholder.info("倒计时结束！")

    # 设置倒计时时长为20秒
    countdown(20)

    #time.sleep(10)
    cookies = driver.get_cookies()
    #print(cookies)
    with open('iqiyi_cookie.txt', 'w', encoding='utf-8') as f:
        f.write(str(cookies))
    st.success("成功获取coolie!!!")

def login(driver):

    time.sleep(1)
    # 1. 从本地的cookie文件中获取cookie
    with open('iqiyi_cookie.txt', encoding='utf-8') as f:
        cookies = eval(f.read())

    # 2. 添加cookie
    for x in cookies:
        driver.add_cookie(x)

    # 3.重新打开网页
    driver.refresh()


if __name__ == '__main__':
    prelogin()
    #login()