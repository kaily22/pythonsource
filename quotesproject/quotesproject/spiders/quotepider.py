import scrapy

#spider 클래스 상속
class QuotepiderSpider(scrapy.Spider):
    name = 'quotespider'
    allowed_domains = ['quotes.toscrape.com/tag/humor']
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        #print(response) #Crawled (200) <GET http://quotes.toscrape.com/tag/humo

        # print(response.text) #소스 가져오기
        # print(response.url)
        # print(response.status)
        # print(response.body) #byte형태
        # print(dir(response))

        #lxml 파싱/selector/파일 저장 간편

        for quote in response.css("div.quote"):
            yield {

                'author':quote.xpath('span/small/text()').get(),
                'text':quote.css('span.text::text').get()
            }
            next_page = response.css('li.next a::attr("href")').get()
            if next_page is not None:
                yield response.follow(next_page,self.parse)






    

