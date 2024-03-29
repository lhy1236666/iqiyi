# _*_ coding=utf-8 _*_

import requests
from urllib.parse import urlencode
import pyhttpx

base_url = 'https://weibo.com/ajax/feed/hottimeline?'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",}

session = pyhttpx.HttpSession()
# res = session.get(url='https://www.baidu.com/', headers=headers)
# print(res.text)

def get_page(page):
    """
    :param page:
    :return:
    """
    # 构造参数字典
    params = {
        'refresh': '2',
        'group_id': '102803',
        'containerid': '102803',
        'extparam': 'discover|new_feed',
        'max_id': page,
        'count': 10
    }
    # 拼接参数与url
    url = base_url + urlencode(params)
    print(url)
    # from selenium import webdriver
    # chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=chrome_driver)
    # driver.get(url)
    # input()
    try:
        res = session.get(url=url, headers=headers)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print('Error:', e.args)


if __name__ == "__main__":

    for page in range(1, 2):
        result = get_page(page)
        print(result)