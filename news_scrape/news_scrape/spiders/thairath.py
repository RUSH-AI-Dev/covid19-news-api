import scrapy
from ..items import NewsScrapeItem
import re
import pandas as pd


class ThairathSpider(scrapy.Spider):
    name = "thairath"

    def start_requests(self):
        df = pd.read_csv('thairath_link.csv')
        urls = list(df['link'])
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        items = NewsScrapeItem()

        body = ''
        p = response.css('p::text').extract()
        date = response.css('.e1ui9xgn2::text').extract_first()
        head = response.css('.e1ui9xgn0::text').extract_first()
        for i in p:
            body = body+i+'\n'
        img = response.css('.evs3ejl11 img::attr(src)').extract_first()
        cat = response.css('.evs3ejl44 a+ a::text').extract_first()

        items['body'] = body
        items['date'] = date
        items['head'] = head
        items['img'] = img
        items['category'] = cat

        yield items
