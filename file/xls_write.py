from openpyxl import Workbook

# 객체 생성
wb = Workbook()

#엑셀 파일이 생성될 때 기본 시트가 하나가 존재함
ws1 = wb.active

#ws1이 가리키는 시트명 변경
ws1.title = "range names"

for row in range(1,40):
    ws1.append(range(600))

# 파일 작성
wb.save("./data/test1.xlsx")
