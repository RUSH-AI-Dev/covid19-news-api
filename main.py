#%%
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from net_api import *
import pandas as pd 
import credentials
import time
import os

#%%
if __name__ == "__main__":

    os.chdir(r'D:/GIT/18_rushai/news-api')
    path = r'chromedriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://www.thairath.co.th/home')
    
    href=[]
    time.sleep(5)
    a = driver.find_elements_by_css_selector('a.breaking-news-link')
    for i in a:
        href.append(i.get_attribute('href'))
        print(i.get_attribute('href'))
    driver.close()
    driver.quit()
    
    df = pd.DataFrame({'link':href})
    df.to_csv('news_scrape/thairath_link.csv',index=False)

    os.chdir(r'D:/GIT/18_rushai/news-api/news_scrape')

    ###################### ต้อง run selenium_thairath ก่อน ######################

    web = ['thairath','dailynews','nation','sanook','voice']

    for i in web:
        os.system(f'scrapy crawl {i} -o output/{i}.xlsx')
        
    os.chdir(r'D:/GIT/18_rushai/news-api/news_scrape')
    insert_voice(filename='output/voice.xlsx')
    insert_dailynews(filename='output/dailynews.xlsx')
    insert_nation(filename='output/nation.xlsx')
    insert_sanook(filename='output/sanook.xlsx')
    insert_thairath(filename='output/thairath.xlsx')
