from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By

import time

if __name__ == '__main__':
    # print('PyCharm')
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    
    service = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(service = service)
    driver.get('https://www.baidu.com')
    try:
        #driver.find_element_by_id('kw').send_keys('python')
        #driver.find_element_by_id('su').click()
        # // *[ @ id = "kw"]//*[@id="kw"]//*[@id="su"]//*[@id="kw"]//*[@id="su"]

        driver.find_element(By.XPATH, '//*[@id="kw"]').click()
        driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('python')
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="su"]').click()
        time.sleep(3)
        print(driver.page_source)
       # print('============================')
    finally:
        time.sleep(3)
        driver.quit()