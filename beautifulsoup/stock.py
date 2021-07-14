#네이버 증권 인기 검색 종목

import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(response.content,"html.parser")

#print(soup.prettify())
##_topItems1 > tr:nth-child(1) > th > a

popular = soup.select_one("div.aside_popular > table.tbl_home")

#print(popular)

# tr 전체 가져오기
popular_tr = popular.select('tr')

print(popular_tr)

#print(popular_tr)
for item in popular_tr:
    # 종목명 태그 모두 가져오기
    stock_name = item.find_all("a")
    # 가격 태그 모두 가져오기
    stock_prcie = item.select("td:nth-of-type(1)")

    if stock_name:
        for idx,name in enumerate(stock_name):
            print(name.string, stock_prcie[idx].string)

