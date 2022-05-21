from selenium import webdriver
from selenium.webdriver.common.by import By

class Country:
    def __init__(self, name, capital, population, area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
        # if "E" in area:
        #     a,b=area.split('E')
        #     self.area=float(a)*(10**int(b))
        # else:
        #     self.area=float(area)

with webdriver.Chrome() as driver:
    driver.get("https://www.scrapethissite.com/pages/simple/")
    country_list = []
    div_list=driver.find_elements(by=By.CLASS_NAME, value='country')
    for div in div_list:
        name=div.find_element(by=By.CLASS_NAME, value='country-name')
        capital=div.find_element(by=By.CLASS_NAME, value='country-capital')
        population=div.find_element(by=By.CLASS_NAME, value='country-population')
        area=div.find_element(by=By.CLASS_NAME, value='country-area')
        country=Country(name, capital, population, area)
        country_list.append(country)

capital_list=[]
for country in country_list:
    capital_list.append(country.capital)
capital_list.sort()     #sorted(capital_list)\
print(capital_list[29])
    
global_pop=0
for country in country_list:
    global_pop += country.population
print(global_pop)
