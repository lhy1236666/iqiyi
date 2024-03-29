
import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import login
import time
def write_string_to_csv(file_path, input_string,i):
    df = pd.DataFrame(input_string)
    if i==1:
        df.to_csv(file_path, index=False, encoding='utf-8')
    else:
        existing_df = pd.read_csv(file_path)
        # 将新数据添加到已有数据的末尾
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        # 将合并后的DataFrame保存为CSV文件
        combined_df.to_csv(file_path, index=False)
    return 0
def hot_actors_to_csv(file_path, input_string):
    df = pd.DataFrame(columns=['Name', 'Role'])
    for i in range(0, len(input_string), 2):
        df = df._append({'Name': input_string[i], 'Role': input_string[i+1]}, ignore_index=True)
    df.to_csv(file_path, index=False)
    return 0
# 创建一个字典
def hot_actors_to_csv1(file_path, input_string):
    df = pd.DataFrame(columns=['Name', 'Role'])
    i=0
    flag=0
    while( i<len(input_string)-1 ):
        if ('导演' in input_string[i+1]) or ('饰' in input_string[i+1]):
            df = df._append({'Name': input_string[i], 'Role': input_string[i+1]}, ignore_index=True)
            i+=2
        else:
            df = df._append({'Name': input_string[i], 'Role': ''}, ignore_index=True)
            i+=1
            flag=1
    if flag:
        df = df._append({'Name': input_string[i], 'Role': ''}, ignore_index=True)
    df.to_csv(file_path, index=False)
    return 0
def get_apppage(driver,action):
    #html=driver.page_source
    #soup = BeautifulSoup(html, 'html.parser')    
    #print(soup)
    hot_num=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.meta-hot > span').text

    #hot_intro=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg > div.qy_tvg_body > div.qy_video_wrap > div.tvg-block > div.Desc_descCont__noKqN > span')
    #action.click(hot_intro).perform()
    #hot_intro1=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg > div.qy_tvg_body > div.qy_video_wrap > div.tvg-block > div.Desc_descCont__noKqN > div.Desc_desc__NiOk_.text-50').text
    print(hot_num)
    #print(hot_intro1)
    for i in range(1,5):
        hot_actors=driver.find_element(By.CSS_SELECTOR,'#j_star_slider_wrap > div > ul > li:nth-child('+str(i)+')').text
        print(hot_actors)
    input()
    driver.stop()
    return 0
def get_message(driver,action):
    try:
        intro_change=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/h2/div')
    except Exception as e:  
        try: 
            intro_change=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/h2/div')
        except:
            get_apppage(driver,action)
            return 0

def filter_str(des_str, res_tr=''):
    """
    过滤除中英文及数字以外的其他字符
    """
    res = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    return res.sub(res_tr, des_str)


def filter_emoji(des_str, res_tr=''):
    """过滤表情"""
    try:
        res = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        res = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return res.sub(res_tr, des_str)

cast_list = [
    '格蕾塔·葛韦格', '导演', '玛格特·罗比', 
    '瑞恩·高斯林', '海伦·米伦', 
    '亚美莉卡·费雷拉',  '威尔·法瑞尔', 
    '迈克尔·塞拉', '凯特·麦克金农', 
    '艾玛·麦肯', 
]
#hot_actors_to_csv1('./data/actors'+str(1)+'.csv', '')
#mapping = {'url': '//www.iqiyi.com/v_151oux8ma9s.html?vfrm=pcw_home&amp;vfrmblk=pcw_home_hot&amp;vfrmrst=pcw_home_hot_title1&amp;r_area=recent_popular&amp;r_source=1001&amp;bkt=hp_bkt_02&amp;e=de9709ef8db0838642104b7ed4d52baf&amp;stype=2', 'name': '唐人街探案2', 'hot_num': '7429', 'introdution': '“唐探宇宙”原班人马惊喜回归！网剧《唐人街探案2》强势来袭，监制及总 编剧陈思诚领衔新锐导演姚文逸、王天尉，匠心打造四个全新悬疑推理单元《天使的旋律》《恶魔的呼吸》《游乐园》《黄金城》。城市之间罪恶涌动，侦探林默（邱泽 饰）、Kiko（尚语贤 饰）谜案 穿梭各显神通。2024，CRIMASTER侦探排行榜重新洗牌！'}
#write_string_to_csv('./data/my_dict_data.csv',mapping,1)
# 从csv文件中读取数据并转换为DataFrame
#df_read = pd.read_csv('./data/my_dict_data.csv')

# 打印读取的DataFrame
#print(df_read)


def get_apppage11(driver):
    action = ActionChains(driver)
    hot_num=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]').text
    print(hot_num)
    change=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg > div.qy_tvg_body > div.qy_video_wrap > div.tvg-block > div.Desc_descCont__noKqN > span')
    action.click(change).perform()
    hot_intro=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg > div.qy_tvg_body > div.qy_video_wrap > div.tvg-block > div.Desc_descCont__noKqN > div.Desc_desc__NiOk_.text-50').text
    print(hot_intro)
    flag=1
    while (1):
        
        hot_actors=driver.find_element(By.CSS_SELECTOR,'#j_star_slider_wrap > div').text
        hot_actors=hot_actors.split('\n')
        if flag:
            actors=hot_actors
            flag=0
        else:
            actors.extend(hot_actors)

        try:
            driver.find_element(By.CSS_SELECTOR,'#j_star_slider_wrap > svg.Star_arrow___2gh0.Star_right__uMKTE.Star_disable__gSVPT')
            break
        except:                 
            right=driver.find_element(By.CSS_SELECTOR,'#j_star_slider_wrap > svg.Star_arrow___2gh0.Star_right__uMKTE')
            #'#j_star_slider_wrap > svg.Star_arrow___2gh0.Star_right__uMKTE.Star_disable__gSVPT'
            action.click(right).perform()
            time.sleep(0.2)

    #print(hot_actors)
    #'#j_star_slider_wrap > div > ul > li:nth-child(1)'
    #'#j_star_slider_wrap > div > ul > li:nth-child(6)'2920

    return 0
# option=Options()
# driver = webdriver.Chrome(options = option)
# action = ActionChains(driver)
# driver.get('https://www.iqiyi.com/v_a5zfxoovko.html?r_area=recent_popular&r_source=1001&bkt=hp_bkt_02&e=acf7c7681b7bd29deffbfeb3f59323c8&stype=2&vfrm=pcw_home&vfrmblk=pcw_home_hot&vfrmrst=pcw_home_hot_float_video_area2')
# #get_message(driver,action)
# login.login(driver)
# get_apppage(driver)


#############
# import time

# timestamp = 1462451334

# #转换成localtime
# time_local = time.localtime(timestamp)
# #转换成新的时间格式(2016-05-05 20:28:54)
# dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

# print (time_local)
import pyhttpx
def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",}
    session = pyhttpx.HttpSession()
    try:
        #发送get请求
        html = session.get(url,headers = headers)
        #配置编码
        if html.status_code == 200: 
            print("成功过获取源代码")
            
    except Exception as e:
        print("获取源代码失败:%s"% e)
    return html.text 

# html=get_html('https://www.iqiyi.com/v_1tea2kmmbls.html?vfrm=new_personalcenter&vfrmblk=order_offline&vfrmrst=click_picture')
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# name='aaaaa'
# name=name.replace("简介",'')
# print(name)



def get_apppage(driver,action):
    m=0
    input()
    try:
        hot_num=driver.find_element(By.XPATH,'//*[@id="plist-body"]/div/div[1]/div[2]/div[2]/div[1]').text
        m=1
    except:
        hot_num=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[4]/span').text

    if m==1:
        hot_intro=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.desc-cont > div.desc.text-50').text
    else:
        hot_intro=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg.ticket > div.qy_tvg_body > div.qy_video_wrap > div.index_cloudMetaWrap__XaOEI > div.Desc_descCont__noKqN > div.Desc_desc__NiOk_.text-50').text
        
    print(hot_num)
    print(hot_intro)
    input()
    #hot_message['hot_num']=[hot_num]
    #hot_message['introdution']=[hot_intro]
    flag=1
    if m==1:
        while (1):
            hot_actors=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.star-block > div').text
            hot_actors=hot_actors.split('\n')
            if flag:
                actors=hot_actors
                flag=0
            else:
                actors.extend(hot_actors)

            try:
                driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.star-block > svg.arrow.right.disable')
                break
            except:                 
                right=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.star-block > svg.arrow.right')

                #'#j_star_slider_wrap > svg.Star_arrow___2gh0.Star_right__uMKTE.Star_disable__gSVPT'
                action.click(right).perform()
                time.sleep(0.2)
    else:
        while (1):
            hot_actors=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.star-block > div').text
            hot_actors=hot_actors.split('\n')
            if flag:
                actors=hot_actors
                flag=0
            else:
                actors.extend(hot_actors)

            try:
                driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.star-block > svg.arrow.right.disable')
                break
            except:                 
                right=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.star-block > svg.arrow.right')

                #'#j_star_slider_wrap > svg.Star_arrow___2gh0.Star_right__uMKTE.Star_disable__gSVPT'
                action.click(right).perform()
                time.sleep(0.2)
    #hot_actors_to_csv(actors,i,reflag)


    return 0

option=Options()
driver = webdriver.Chrome(options = option)
action = ActionChains(driver)
driver.get('https://www.iqiyi.com/v_keg4sfvk18.html?r_area=recent_popular&r_source=1002&bkt=hp_bkt_02&e=d386468ea01f8de633091d82b21c40aa&stype=2&vfrm=pcw_home&vfrmblk=pcw_home_hot&vfrmrst=pcw_home_hot_float_video_area4')
#get_message(driver,action)
login.login(driver)
get_apppage(driver,action)