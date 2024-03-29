from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ContentPageParser():
    def __init__(self, content_page_url) -> None:
        self.content_url = content_page_url # 抓取content_page_url页面上全部的图片url
        self.img_src = []                   # 保存当前页面上所有的图片url
    
    def visit_content_page_with_firefox(self):
        option = FirefoxOptions()
        # 设置浏览器为无头模式，使用过程中不会弹出浏览器页面
        option.headless = True
        self.driver = Firefox(options=option)
        try:
            # 打开待抓取的url页面
            self.driver.get(self.content_url)
            # 设置灵活等待，最长等待10s，轮询间隔为1s
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
            # 使用css选择器进行元素定位，直到元素可见为止
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[class="showimg"]')))
            # 使用css选择器查找所有元素
            imgs = self.driver.find_elements(By.CSS_SELECTOR, 'img[class="showimg"]')
            # 提取所有图片的url
            for img in imgs:
                self.img_src.append(img.get_attribute('src'))
        except Exception as e:
            print(repr(e))
        finally:
            # 关闭webdriver
            self.driver.close() 
    
    def get_img_src(self):
        return self.img_src
    
if __name__ == '__main__':
    content_parser = ContentPageParser('https://xxx/content_48495.html')
    content_parser.visit_content_page_with_firefox()
    img = content_parser.get_img_src()
    print(img)




def get_message(driver,action):
    try:
        hot_num=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]').text
        hot_message['hot_num']=hot_num  
        intro_change=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/h2/div')
        action.click(intro_change).perform()
        time.sleep(1)
        introdution=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg > div.qy_tvg_body > div.qy_video_wrap > div.base_layerWrapper__McyRW.qyp-slidein-enter-done > div.base_panelContent__LiEuQ > div.infoLayer_intro-wrap__hT3QL > div.infoLayer_text__y8K_q').text
        hot_message['introdution']=introdution
        print(hot_message)
        get_actors(driver)
    except Exception as e:
        intro_change=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/h2/div')
        action.click(intro_change).perform()
        time.sleep(1)
        hot_num=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[7]/div[2]/div[1]/div[1]/div[2]/div[2]').text
        numbers = re.findall(r'\d+', hot_num)
        hot_message['hot_num']=numbers[0]  
        introdution=driver.find_element(By.CSS_SELECTOR,'#__next > div > div.qy_app_cont > div.qy_app_warp > div.qy_tvg.ticket > div.qy_tvg_body > div.qy_video_wrap > div.base_layerWrapper__McyRW.qyp-slidein-enter-done > div.base_panelContent__LiEuQ > div.infoLayer_intro-wrap__hT3QL > div.infoLayer_text__y8K_q').text
        hot_message['introdution']=introdution
        print(hot_message)

    
    return 0