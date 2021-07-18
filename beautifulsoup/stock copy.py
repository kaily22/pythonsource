#네이버 증권 인기 검색 종목

import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(response.content,"html.parser")

#print(soup.prettify())
##_topItems1 > tr:nth-child(1) > th > a
#container > div.aside > div > div.aside_area.aside_stock > table
global_stock = soup.select("div.aside_stock > table.tbl_home > tbody tr")

print(global_stock)

#tr 전체 가져오기
# popular_tr = global_stock.select('tr')

# print(popular_tr)

# #print(popular_tr)
for item in global_stock:
    # 종목명 태그 모두 가져오기
    stock_name = item.find_all("a")
    # 지수 인덱스 가져오기
    stock_index = item.select_one("td")
    #지수 포인트 가져오기
    stock_point = item.select_one("td:nth-of-type(2)")

    print(stock_name.string, stock_index.string, stock_point.text)

