import scrapy
from ..items import NewsScrapeItem
import re

class SanookSpider(scrapy.Spider):
    name = "sanook"

    def start_requests(self):
        urls = ['https://www.sanook.com/news/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css('.col-lg-4 .text-color-news a::attr(href)').extract()
        for i in urls:
            i = 'https:'+i
            yield scrapy.Request(url=i, callback=self.parse_news)

        
    def parse_news(self, response):
        items = NewsScrapeItem()

        date = response.css('time.jsx-2376132709::text').extract_first()
        head = response.css('.jsx-2761676397.title::text').extract_first()
        
        img = response.css('.jsx-2954975791').xpath('img/@src').extract_first()
        
        cat = response.css('.jsx-2080913917.text-color-news::text').extract_first()
        body = response.css('strong::text , #EntryReader_0 p::text').extract()

        items['body'] = body
        items['date'] = date
        items['head'] = head
        items['img'] = img
        items['category'] = cat

        yield items
#%%