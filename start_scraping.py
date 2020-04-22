#%%
import os

os.chdir(r'D:/GIT/01_Navy/09_bot/news_scrape')

###################### ต้อง run selenium_thairath ก่อน ######################

web = ['thairath','dailynews','nation','sanook','voice']

for i in web:
    os.system(f'scrapy crawl {i} -o output/{i}.xlsx')