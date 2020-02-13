
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
try:
    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
    elem=driver.find_element_by_id('revolution_main_table')
    #print(elem.text)
    lis=elem.find_elements_by_class_name('list_title')
    #lis=trs.find_elements_by_tag_name('td')
    
    for li in lis:
        print(li.text)
except Exception as e:
    print(e)    
finally:
    driver.quit()
