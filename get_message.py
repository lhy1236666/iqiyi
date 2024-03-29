from selenium import webdriver
import streamlit as st
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
import time
import login
import pandas as pd
import get_comment 


hot_message = {}

def switch(sreach_windows,all_handles,driver,action,i,flag=0):
        driver.switch_to.window(all_handles[1])
        filepath='./data/my_dict_data.csv'
        #time.sleep(1)
        if flag==1:
            try:
                name=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.qy-side-head > div').text
            except:
                name=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.head-flex > div.title-cont > div.title').text
            name=name.replace("简介",'')

            url=driver.current_url
            get_comment.get_comment(str(url),i,1)
            hot_message['id']=[str(i)]
            hot_message['url']=[str(url)]
            hot_message['name']=[str(name)]
            filepath='./data/redata/revideo_data.csv'
        get_message(driver,action,i,flag)
        hot_message_to_csv(filepath,hot_message,i)
        driver.close()
        driver.switch_to.window(sreach_windows)
        return 0

def hot_actors_to_csv(input_string, num,reflag=0):
    #print(reflag)
    if reflag==1:
        file_path='./data/redata/actors/actors'+str(num)+'.csv'
    else:
        file_path='./data/actors/actors'+str(num)+'.csv'
    df = pd.DataFrame(columns=['Name', 'Role'])
    i=0
    flag=0
    while( i<len(input_string)-1 ):
        if ('导演' in input_string[i+1]) or ('饰' in input_string[i+1]) or ('主演' in input_string[i+1]):
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
    
def hot_message_to_csv(file_path, input_string,i):
    df = pd.DataFrame(input_string)
    if i==1:
        df.to_csv(file_path, index=False)
    else:
        existing_df = pd.read_csv(file_path)
        # 将新数据添加到已有数据的末尾
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        # 将合并后的DataFrame保存为CSV文件
        combined_df.to_csv(file_path, index=False)
    return 0

def get_apppage(driver,action,i,reflag):
    m=0
    try:
        hot_num=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.fun.ticket > div:nth-child(1)').text
        
    except:
        hot_num=driver.find_element(By.XPATH,'//*[@id="plist-body"]/div/div[1]/div[2]/div[2]/div[1]').text
        m=1
    if m==1:
        hot_intro=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.desc-cont > div.desc.text-50').text
    else:
        hot_intro=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.desc-cont > div.desc.text-50').text
    # print(m)
    # print(hot_num)
    # print(hot_intro)
    # input()
    hot_message['hot_num']=[hot_num]
    hot_message['introdution']=[hot_intro]
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
    hot_actors_to_csv(actors,i,reflag)


    return 0
    

def get_message(driver,action,i,reflag):

    try:
        change=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.desc-cont > span')
        action.click(change).perform()
        get_apppage(driver,action,i,reflag)
        return 0
    except:
        try:
            intro_change=driver.find_element(By.XPATH,'//*[@id="plist-body"]/div/div[1]/div[2]/div[1]/div[2]')
            
        except Exception as e:  
            try: 
                intro_change=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/h2/div')
            except:
                try:
                    change=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.desc-cont > span')
                                                            #'#plist-body > div > div.hw-full > div.ticket-meta-cont > div.desc-cont > span'
                    action.click(change).perform()
                    get_apppage(driver,action,i,reflag)
                    return 0
                except:
                    print('=======================================================')
                    print('error:此页面暂未分析')
                    hot_message['hot_num']=['']
                    hot_message['introdution']=['']
                    
                    hot_actors_to_csv('',i,reflag)
                    #get_apppage(driver)
                    return 0

    hot_num=driver.find_element(By.CSS_SELECTOR,'#plist-body > div > div.hw-full > div.meta-cont > div.meta-hot > span').text

    action.click(intro_change).perform()
    time.sleep(1)
    hot_html=driver.page_source
    hot_soup = BeautifulSoup(hot_html, 'html.parser')
    #hot_num=hot_soup.find_all('div',class_='infoLayer_type__iH4IM')

    hot_intro=hot_soup.find_all('div',class_='text')

    hot_actors=hot_soup.find_all('div',class_='content')
    actors = re.findall(r'title="([^"]+)', str(hot_actors))
    intro=re.search(r'4="">([^<]+)', str(hot_intro))
    if intro is None:
        hot_message['introdution']=['']
    else:
        hot_message['introdution']=[intro.group(1)]
    hot_message['hot_num']=[hot_num]
    

    #print(hot_message)
    #print(actors)
    
    hot_actors_to_csv(actors,i,reflag)
    #print(actors)
    return 0
    



def get_hot(driver):
    action = ActionChains(driver)
    sreach_windows = driver.current_window_handle
    
    #print(sreach_windows)
    #time.sleep(1)
    try:
        close=driver.find_element(By.CSS_SELECTOR,'#__layout > div > div.popup-recommend > div.fixed-box > div')
        action.move_to_element(close).move_by_offset(5,5).click().perform()
        print('出现预约弹窗')
    except:
        try: 
            close=driver.find_element(By.CSS_SELECTOR,'body > div.header__ele > div:nth-child(3) > div.header__promotion__popup.bTest > img')
            action.move_to_element(close).move_by_offset(5,5).click().perform()
        except:
            True
    #driver.execute_script("$(arguments[0]).click()",close)
    #print(close)
    #input()
    #driver.execute_script("arguments[0].click", close)
    

    try:
        html=driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        for i in range(1,11):
            #hot_message={}
            index='pcw_home_hot_title'+str(i)
            #print(index)
            a = soup.find_all('a', rseat=index)
            result = re.search(r'href="([^"]+)', str(a))
            url1=result.group(1)
            get_comment.get_comment(url1,i)
            hot_message['id']=[str(i)]
            hot_message['url']=[str(url1)]
            name = re.search(r'title="([^"]+)', str(a))
            #print(result.group(1))
            hot_message['name']=[str(name.group(1))]
            if re.search(r'live', result.group(1)):

                print("热播第"+str(i)+"条为直播")
                #name = re.search(r'title="([^"]+)', str(a))
                #write_string_to_file('./data/热播视频目录.txt',str(name.group(1))+' 直播live'+'\n')
                #hot_message['name']=[str(name.group(1))]
                hot_message['hot_num']=['']
                hot_message['introdution']=['live']

                hot_actors_to_csv('',i)
                hot_message_to_csv('./data/my_dict_data.csv',hot_message,i)
            else:
                
                #write_string_to_file('./data/热播视频目录.txt',str(name.group(1))+'\n')
                
                #time.sleep(2)
                
                if i>=6:
                    change=driver.find_element(By.CSS_SELECTOR,'#title > div > div.qy-mod-nav-link > div > span.turn.turn-right > svg')
                    action.click(change).perform()
                hotimage=driver.find_element(By.CSS_SELECTOR,'#adSkinInner > div.ph-skin-wrap > div.content-wrap > div > div:nth-child(2) > div > div > div > div.qy-mod-list > ul > li:nth-child('+str(i)+') > div > div.qy-mod-link-wrap > a')
                
                action.click(hotimage).perform()
                time.sleep(2)
                all_handles = driver.window_handles
                #print(all_handles)
                switch(sreach_windows,all_handles,driver,action,i)

    finally:
        time.sleep(1)
        driver.quit()
        return 0

def get():
    with st.spinner("正在获取热播视频信息..."):
        option=Options()
        option.add_argument('--headless')
        option.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options = option)
        driver.get('https://www.iqiyi.com/')
        #driver.implicitly_wait(10)
        with st.spinner("正在自动登录..."):
            login.login(driver)
        st.success('自动登录成功！！！')
        get_hot(driver)
    get_success=st.empty()
    get_success.success('获取信息成功！！！')


if __name__ == '__main__':
    option=Options()
    #option.add_argument('--headless')
    option.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = option)
    driver.get('https://www.iqiyi.com/')
    login.login(driver)
    get_hot(driver)

                



    