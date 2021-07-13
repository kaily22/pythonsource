import urllib.request as req

# 파일 URL
file_url="https://search1.kakaocdn.net/argon/0x200_85_hr/77obNfwaRKN"


# 다음 메인페이지 URL
html_url = "https://www.daum.net" #urllib.error.URLError

#다운 받을 경로
save_img="c:/dog.jpg"
save_html="c:/daum.html"

try:
    file1, header1 = req.urlretrieve(file_url,save_img)
    file2, header2 = req.urlretrieve(html_url,save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("다운로드 성공")