from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import NamedTuple


class Record(NamedTuple):
    name:str
    year:int
    wins:int
    losses:int

with webdriver.Chrome() as driver:
    driver.get("https://www.scrapethissite.com/pages/forms/")

    input_e=driver.find_element(by=By.ID, value='q')
    search_e=driver.find_element(by=By.XPATH, value='//*[@id="hockey"]/div/div[4]/div/form/input[2]')

    input_e.send_keys('New')
    search_e.click()

    ul=driver.find_element(by=By.CLASS_NAME, value='pagination')
    a_list=ul.find_elements(by=By.TAG_NAME, value='a')
    
    record_list=[]
    url_list=[]

    for a in a_list[:-1]:
        url_list.append(a.get_attribute('href'))

    for url in url_list:
        driver.get(url)
        tbody=driver.find_element(by=By.TAG_NAME, value='tbody')
        team_list=tbody.find_elements(by=By.CLASS_NAME, value='team')
        for team in team_list:
            name=team.find_element(by=By.CLASS_NAME, value='name').text
            year=team.find_element(by=By.CLASS_NAME, value='year').text
            wins=team.find_element(by=By.CLASS_NAME, value='wins').text
            losses=team.find_element(by=By.CLASS_NAME, value='losses').text
            record=Record(
                name=name,
                year=int(year),
                wins=int(wins),
                losses=int(losses))
            record_list.append(record)
