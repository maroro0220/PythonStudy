
from selenium import webdriver #for crawling
from selenium.webdriver.common.keys import Keys #for using 'Enter'
driver = webdriver.Chrome('chromedriver.exe')
try:
    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    elem=driver.find_element_by_id('keyword')
    elem.send_keys('러닝화')
    elem.send_keys(Keys.RETURN)
    elem=driver.find_element_by_id('revolution_main_table')
    tb=elem.find_elements_by_tag_name('table')
    for tab in tb:
        lis=tab.find_elements_by_tag_name('a')
    #lis=elem.find_elements_by_class_name('list_title')
        for li in lis:
            if li.text:
                print(li.text)
    #input()
except Exception as e:
    print(e)    
finally:
    driver.quit()
