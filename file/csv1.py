# csv 파일 읽기
import csv

with open("./data/sample1.csv","r") as f:
    reader = csv.reader(f)

    print(reader)  #<_csv.reader object at 0x0000016D70211820>
    print(type(reader)) #<class '_csv.reader'>
    #print(dir(reader))

    next(reader) #헤더명 없애기
    for c in reader:
        print(c)


