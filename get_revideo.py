
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import login
import get_message
import time
def get_revideo_message(driver,action):
    sreach_windows = driver.current_window_handle
    #js="""document.getElementsByClassName("plistAd_ad912__ipU_T")[0].style.display='block';"""
    #driver.execute_script(js) 
    time.sleep(2) 
    #input()
    for j in range(1,12):
        if j == 5:
            continue
        try:
            path="""//*[@id="80521_listbox_cnxh"]/div[3]/div[""" + str(j)+']'
            video=driver.find_element(By.XPATH,path)
        except:
            path='#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg > div.qy_tvg_body > div.qy_video_wrap > div:nth-child(7) > div.plistVlist_list__OSxt6.tvg-block.plistVlist_vertical__XejU7 > div:nth-child('+str(j)+')'
            '#\38 0521_listbox_cnxh > div.qy-play-list > div:nth-child(1)'
            video=driver.find_element(By.CSS_SELECTOR,path)
        action.click(video).perform()

        #input()
        #
        all_handles = driver.window_handles
        #driver.execute_script("arguments[0].scrollIntoView();",video)
        if j>5:
            num=j-1
        else:
            num=j
        time.sleep(2)
        get_message.switch(sreach_windows,all_handles,driver,action,num,1)
        
    time.sleep(1)
    driver.quit()

    return 0

def get_veideo(url):
    url='https:'+url
    option=Options()
    option.add_argument('--headless')
    option.add_argument("--window-size=1960,1080")
    driver = webdriver.Chrome(options = option)
    action = ActionChains(driver)
    driver.get(url)
    #driver.implicitly_wait(10)
    #get_message(driver,action)
    login.login(driver)
    try:
        driver.find_element(By.CSS_SELECTOR,'#f78912e15').click()
    except:
        i=1
    #input()
    get_revideo_message(driver,action)



if __name__ == "__main__":
    #df = pd.read_csv('./data/my_dict_data.csv')    
        #url = df[df['id'] == i]['url'].values[0]
    url='https://www.iqiyi.com/v_1pj3ayb1n70.html?vfrm=pcw_home&amp;vfrmblk=pcw_home_hot&amp;vfrmrst=pcw_home_hot_title10&amp;r_area=recent_popular&amp;r_source=1002&amp;bkt=hp_bkt_02&amp;e=e5c96fb6fda24ae9c20558aba7f6191e&amp;stype=2'
    #print(url)
    option=Options()
    #option.add_argument('--headless')
    option.add_argument("--window-size=1960,1080")
    driver = webdriver.Chrome(options = option)
    action = ActionChains(driver)
    driver.get(url)
    #get_message(driver,action)
    login.login(driver)
    try:
        driver.find_element(By.CSS_SELECTOR,'#f78912e15').click()
    except:
        i=1
    #input()
    get_revideo_message(driver,action)

