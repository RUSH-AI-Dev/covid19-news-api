import scrapy
from ..items import NewsScrapeItem
import re


class DailyNewsSpider(scrapy.Spider):
    name = "dailynews"

    def start_requests(self):
        # df = pd.read_csv('link.csv')
        urls = ['https://www.dailynews.co.th/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        all_div = response.css('#latest-news .content')

        # link=[]
        for i in all_div:
            url = 'https://www.dailynews.co.th'+i.css('a::attr(href)').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_news)

        

    def parse_news(self, response):
        items = NewsScrapeItem()

        date = response.css('.date::text').extract_first()
        head = response.css('#news-article .title::text').extract_first()
        img = response.css('#article-slide .slide-img::attr(src)').extract_first()
        img = 'https://www.dailynews.co.th'+img
        cat = response.css('#page-nav li~ li+ li a::text').extract_first()
        body = ''
        b = response.css('.content-all span::text').extract()
        for i in b:
            body=body+i
        if len(b) == 0:
            b = response.css('.content-all::text').extract()
            for i in b:
                body=body+i

        items['body'] = body
        items['date'] = date
        items['head'] = head
        items['img'] = img
        items['category'] = cat

        yield items
#%%