import scrapy


class Gspider2Spider(scrapy.Spider):
    #스파이더명(중복은 x)
    name = 'gspider2'
    #크롤리이 허용된 도메인들
    allowed_domains = ['www.gmarket.co.kr','naver.com','daum.net']
    
    #start_urls에 기록된 url에 대한 요청을 생성하는 start_request()호출되어
    #크롤링을 시작하고 결과에 대해서 parse() 함수가 호출됨
    
    start_urls = ['https://corners.gmarket.co.kr',
    'https://www.naver.com','https://www.daumn.net']

    def parse(self, response):
        print(response)
    

