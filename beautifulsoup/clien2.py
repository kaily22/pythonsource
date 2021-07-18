import requests
from bs4 import BeautifulSoup
import xlsx_write as excel

# clien 사이트의 팁과 강좌 게시판의 1~5페이지 타이틀 크롤링

#range(5) => 0~4, range(1,11)
for page_num in range(5):
    if page_num == 0:  # 팁과 강좌 첫 페이지
        response = requests.get("https://www.clien.net/service/board/lecture")
    
    else: # 2~5page 
        response = requests.get("https://www.clien.net/service/board/lecture?&od=T31&category=0&po="+str(page_num))

    soup = BeautifulSoup(response.content,'html.parser')
    
    #타이틀 찾기
    titles = soup.select("span.subject_fixed")

    # 비어 있는 리스트 생성
    board_list = list()

    for title in titles:
        #print(title.string.strip())
        board_title = [title.string.strip()]
        print(board_title)

        board_list.append(board_title)
        #['아마존(미국) 배송대행한 경우의 반품 경험']
        # #['영국 델타 변이에 의한 사망자 vs 접종별, 연령대 별 비교']

    excel.write_excel_template("clien2.xlsx","팁과 강좌" ,board_list)

