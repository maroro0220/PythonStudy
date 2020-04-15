
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
my_id="maro7913"
my_pw="142435z!"
while True:
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('https://m.work.go.kr/event/eventContent.do?eventNo=533&scrollYn=Y')
        driver.implicitly_wait(10) # seconds
        print("again")
        #pop up close
        btn=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_close')))
        #btn=driver.find_element_by_class_name('btn_close')
        btn.click()
        time.sleep(1)
        #driver.implicitly_wait(10) # seconds
        btn=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_login')))    
        #btn=driver.find_element_by_class_name('btn_login')
        btn.click()
        time.sleep(1)
        #driver.implicitly_wait(10) # seconds
        driver.find_element_by_name('userId').send_keys(my_id)
        driver.find_element_by_name('password').send_keys(my_pw)
        
        time.sleep(1)
        btn=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginBtn')))   
        #btn=driver.find_element_by_id('loginBtn')
        btn.click()
        time.sleep(1)
        #btn=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'cancelBtn')))   
        #btn=driver.find_element_by_id('cancelBtn')
        #btn.click()
        #driver.implicitly_wait(10) # seconds
        while True:
            min = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'min')))
            #min=driver.find_element_by_class_name('min')
            #sec=driver.find_element_by_class_name('sec')
            ms=min.text
            time.sleep(1)
            print(ms)
            time.sleep(5)
            #if(ms=='0' and ss=='0'):
            while(ms=='0'):
                print("Now")
                sec = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'sec')))
                ss=sec.text
                print(ss)
                if ss=='0':
                    btn=driver.find_element_by_id('btnCoupon')
                    btn.click()
                    alert = driver.switch_to.alert
                    alert.accept()
                    break
                time.sleep(3)
            #print("no")
            #driver.quit()
            print("end")
            time.sleep(600)
        #time.sleep(26*60)
        #print(elem.text)
        #lis=elem.find_elements_by_class_name('list_title')
        #lis=trs.find_elements_by_tag_name('td')
        
        #for li in lis:
        #    print(li.text)
    except Exception as e:
        print(e)
        driver.quit()    
        continue
#finally:
    #driver.quit()
