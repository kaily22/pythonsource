import urllib.request as req

#urlopen = 메모리에 내용을 올려놓고 분석

url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain"

try:
    #response = req.urlopen(url).read().decode("euc-kr")
    
    #헤더 정보랑 컨텐츠 정보 따로 출력
    response = req.urlopen(url)
    contents = response.read().decode("euc-kr")
except:
    print("에러발생")
else:
    print("header - {} ".format(response.info()))
    print(contents[:3000])


