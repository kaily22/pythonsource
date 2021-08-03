import scrapy
from ..items import ComputerworldItem

class WorldSpider(scrapy.Spider):
    name = 'world'
    #allowed_domains = ['www.computerworld.com/news']
    start_urls = ['http://www.computerworld.com/news/']

    def parse(self, response):
        
    #링크 주소 추출하기
     article_links = response.css("div.river-well figure a::attr('href')").getall()

    #이미지 주소 추출하기
     article_img = response.css("div.river-well figure a img::attr('data-original')").getall()
    
    #타이틀 내용 추출
     article_title = response.css("div.river-well div.post-cont h3 a::text").getall()

     #print(article_links)
    #  for i, article in enumerate(article_links):
    #     # print("{} {}".format(article,article_title[i]))
    #     #print("{} {} {}".format(article,article_title[i],article_img[i]))

    #     title = article_title[i]
    #     link = article
    #     img_url = article_img[i]

    #     yield {
    #         'title': title,
    #         'link': link,
    #         'url': img_url
    #     }
    # 
     for url in article_links:
        yield scrapy.Request(response.urljoin(url),self.parse_article)

    def parse_article(self,response):
        print(response.url) 

        #이미지 주소 추출하기
        img_url = response.css("figure img::attr('data-original')").get()
    
        #타이틀 내용 추출
        title = response.css("h1::text").getall()

        # 본문 내용 추출

        contents = ''.join(response.css("#drr-container p::text").getall())


        item = ComputerworldItem()
        item['title'] = title
        item['contents'] = contents
        item['url'] = img_url

        #yield : 리턴의 개념

        yield item

        # yield {
        #     'title': title,
        #     'contents': contents,
        #     'url': img_url
        # }
    



