import csv
from os import read

with open("./data/sample2.csv","r") as f:
    reader = csv.reader(f,delimiter="|")

    next(reader) #제목행 제거
    for c in reader:
        print(c)
    