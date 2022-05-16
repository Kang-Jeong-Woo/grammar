from lib2to3.pgen2 import driver
from matplotlib.pyplot import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#with webdriver.Chrome() as driver:
driver=webdriver.Chrome()
driver.implicitly_wait(10)                                  #새로운 page를 로딩 할 때마다 최대!! N초만큼 기다림.
driver.get ('https://cafe.naver.com/kkangstylist?iframe_url=/ArticleList.nhn%3Fsearch.clubid=29598309%26search.menuid=72%26search.boardtype=I')
    #a= driver.find_element_by_tag_name('body')             #부모요소를 선택 시 자식요소까지 전부 딸려옴.
    #b= driver.find_element_by_tag_name('p')                #첫번 째 p를 만나면 즉시 종료.
    #e_list= driver.find_elements_by_tag_name('p')
    #for e in e_list:
    #    print(e.text)                                      #가져온 요소추출은 .text로  
    #c= e_list[1]                                           #원하는 요소
    # d=driver.find_element_by_tag_name('div')\
    #     .find_element_by_tag_name('p')                    #요소 내 요소를 선택
    # print(d.text)
    

    #X.path 문법
    #/html/body/p
    #//p 모든 하위 노드를 반환
    #//div/p
    #/html/body//*
    #//p[@class='bold']
    
    #x.path 활용
    #xpath=//p
    #a=driver.find_element_by_xpath(xpath)
    #xpath2 = "//*[contains(@class,'big')]"                 #클래스 중 big은 전부 가져 옴

    #기다림.
e= WebDriverWait(driver, 10 ).until(
    EC.presence_of_all_elements_located((By.ID, 'id_name')))#명시적 기다리기. ID대신 XPATH나 CLASS, TAG 등 모두 가능.
    #element_to_be_clickable
    
xpath="//[@class,'article-album-sub'']/img"
img_list=driver.find_element_by_xpath(xpath)
print(img_list)