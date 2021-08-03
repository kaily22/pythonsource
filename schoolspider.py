import scrapy


class SchoolspiderSpider(scrapy.Spider):
    name = 'schoolspider'
    allowed_domains = ['www.w3schools.com']
    start_urls = ['http://www.w3schools.com/']

    def parse(self, response):
        pass
