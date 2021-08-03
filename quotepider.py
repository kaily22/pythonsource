import scrapy


class QuotepiderSpider(scrapy.Spider):
    name = 'quotepider'
    allowed_domains = ['quotes.toscrape.com/tag']
    start_urls = ['http://quotes.toscrape.com/tag/']

    def parse(self, response):
        pass
