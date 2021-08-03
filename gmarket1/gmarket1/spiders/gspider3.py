import scrapy


class Gspider3Spider(scrapy.Spider):
    #스파이더명(중복은 x)
    name = 'gspider3'
    #크롤리이 허용된 도메인들
    # allowed_domains = ['www.gmarket.co.kr','naver.com','daum.net']
    
    #start_urls에 기록된 url에 대한 요청을 생성하는 start_request()호출되어
    #크롤링을 시작하고 결과에 대해서 parse() 함수가 호출됨
    
    # start_urls = ['https://corners.gmarket.co.kr',
    # 'https://www.naver.com','https://www.daumn.net']

    def start_requests(self):
        yield scrapy.Request('https://www.gmarket.co.kr',self.parse)
        yield scrapy.Request('https://www.naver.com',self.parse)
        yield scrapy.Request('https://www.daum.net',self.parse)
        
    def parse(self, response):
        # print(response.url)
        
        if response.url.find('gmarket'):
            yield{
                'sitemap':response.url,
                'contents':response.text[:1000]
            }
        elif response.url.find('naver'):
            yield{
                'sitemap':response.url,
                'contents':response.text[:1000]
            }
        else:
             yield{
                'sitemap':response.url,
                'contents':response.text[:1000]
            }
    

