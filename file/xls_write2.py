from openpyxl import Workbook

# 객체 생성
wb = Workbook()
print(wb.sheetnames)

#시트 삭제
wb.remove(wb['Sheet'])

#새로운 시트 생성
