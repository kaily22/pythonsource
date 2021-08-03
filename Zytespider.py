import scrapy


class ZytespiderSpider(scrapy.Spider):
    name = 'Zytespider'
    allowed_domains = ['zyte.com']
    start_urls = ['http://zyte.com/']

    def parse(self, response):
        pass
