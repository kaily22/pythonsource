#2차원 리스트 => csv 에 저장

import csv

list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

with open("./data/numbers2.csv","w", newline="") as f:
    writer = csv.writer(f)
    #한꺼번에 데이터 쓰기
    writer.writerows(list1)
