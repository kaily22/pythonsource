import urllib.request as request
from urllib.error import URLError
from fake_useragent import UserAgent

url="https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=374&aid=0000250556"

try:

    # 객체 생성
    userAgent = UserAgent()

    #header 생성
    headers = {
        'User-agent' : userAgent.chrome
    }

    #host명과 User-agent 확인
    request_url = request.Request(url,headers = headers)
    response = request.urlopen(request_url).read()
except URLError as e:
    print(e)
else:
    print(response[:2000])
    print(request_url.header_items())
