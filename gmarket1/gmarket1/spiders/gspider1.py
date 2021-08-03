import scrapy


class Gspider1Spider(scrapy.Spider):
    name = 'gspider1'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['https://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        titles = response.css('div.best-list ul:not(.plus) li a::text').getall()

        for idx,title in enumerate(titles):
            print("{}.{}".format(idx,title))
            yield{
                "no":idx,
                "title":title
                
            }
