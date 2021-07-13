import urllib.request as request

movie_info = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20210711"

#다운로드 받아서 파일로 저장

try:
    data = request.urlopen(movie_info).read().decode("utf-8")
except:
    print("error")
else:
    with open('c:/movie.txt','w') as f:
        f.write(data)