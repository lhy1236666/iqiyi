from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
import time

def prelogin():
    # 1. 创建浏览器打开需要自动登录的网页
    service = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    driver.get('https://weibo.com/login.php')

    # 2. 留足够长的时间给人工完成登录
    # （完成登录的时候必须保证浏览器对象指向的窗口能够看到登录成功的效果）
    
    # 进入网页后会有登录提示，手动扫码登录成功后，回到pycharm的输出区输入任意
    # 字符给input，方便我们知道执行到什么地方了
    input('已经完成登录:')

    # 3. 获取浏览器cookie保存到本地文件
    cookies = driver.get_cookies()
    with open('weibo_cookie.txt', 'w', encoding='utf-8') as f:
        f.write(str(cookies))


def login():
    service = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    driver.get('https://www.weibo.com')
    time.sleep(10)
    # 1. 从本地的cookie文件中获取cookie
    with open('weibo_cookie.txt', encoding='utf-8') as f:
        cookies = eval(f.read())
        #print('======')

    # 2. 添加cookie
    for x in cookies:
        driver.add_cookie(x)

    # 3.重新打开网页
    driver.refresh()

    input()

if __name__ == '__main__':
#prelogin()
    login()