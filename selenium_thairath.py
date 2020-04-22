# %%
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# %%
path = r'D:/GIT/18_rushai/news-bot/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(executable_path=path)
driver.get('https://www.thairath.co.th/home')
# %%
href=[]
time.sleep(5)
a = driver.find_elements_by_css_selector('a.breaking-news-link')
for i in a:
    href.append(i.get_attribute('href'))
    print(i.get_attribute('href'))
driver.close()
driver.quit()
# %%
df = pd.DataFrame({'link':href})
df.to_csv('news_scrape/thairath_link.csv',index=False)
