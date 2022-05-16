from lib2to3.pgen2 import driver
from matplotlib.pyplot import get
from selenium import webdriver

#with webdriver.Chrome() as driver:
driver=webdriver.Chrome()
driver.get ('https://cafe.naver.com/kkangstylist')
    #a= driver.find_element_by_tag_name('body')            #부모요소를 선택 시 자식요소까지 전부 딸려옴.
    #b= driver.find_element_by_tag_name('p')               #첫번 째 p를 만나면 즉시 종료.
    #e_list= driver.find_elements_by_tag_name('p')
    #for e in e_list:
    #    print(e.text)                                      #가져온 요소추출은 .text로  
    #c= e_list[1]                                          #원하는 요소
    # d=driver.find_element_by_tag_name('div')\
    #     .find_element_by_tag_name('p')                     #요소 내 요소를 선택
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
    #xpath2 = "//*[contains(@class,'big')]"                 #클래스 중 big은 전부 가져 옴.
