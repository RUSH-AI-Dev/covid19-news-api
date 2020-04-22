import scrapy
from ..items import NewsScrapeItem
import re



class NationSpider(scrapy.Spider):
    name = "nation"

    def start_requests(self):
        urls = ['https://www.nationtv.tv/main/content/latest/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        

        all_div = response.css('.mb-4')
        for i in all_div:
            url = i.xpath("div/div/div/a/@href").extract_first()
            
            yield scrapy.Request(url=url, callback=self.parse_news)

        

    def parse_news(self, response):
        items = NewsScrapeItem()

        date = response.css('.article-date::text').extract_first()
        head = response.css('.article-title::text').extract_first()
        
        img = response.css('.article-feature-image img::attr(src)').extract_first()
        
        cat = response.css('.breadcrumb-item:nth-child(3) a::text').extract_first()
        body = ''
        b = response.css('.article-body p::text').extract()
        for i in b:
            body=body+i+'\n'

        items['body'] = body
        items['date'] = date
        items['head'] = head
        items['img'] = img
        items['category'] = cat

        yield items
#%%