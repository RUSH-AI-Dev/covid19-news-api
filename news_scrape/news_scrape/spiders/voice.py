import scrapy
from ..items import NewsScrapeItem
import re

class VoiceSpider(scrapy.Spider):
    name = "voice"

    def start_requests(self):
        urls = ['http://www.voicetv.co.th/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css('.columns+ .is-multiline .title a::attr(href)').extract()
        for i in urls:
            i = 'http://www.voicetv.co.th'+i
            yield scrapy.Request(url=i, callback=self.parse_news)

        

    def parse_news(self, response):
        items = NewsScrapeItem()

        date = response.css('.last::text').extract_first()
        head = response.css('.nuxt-link-exact-active::text').extract_first()
        
        img = response.css('div.hero-section').xpath('div/@style').extract_first()
        img = re.search(r"url\('(.*?)'\);", img).group(1) + '.jpg'
        cat = response.css('.info .topic a::text').extract_first()
        body = response.css('.excerpt::text , p::text , p a::text').extract()

        items['body'] = body
        items['date'] = date
        items['head'] = head
        items['img'] = img
        items['category'] = cat

        yield items
#%%