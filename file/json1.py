import json

data="""
  {
      "id" : "01",
      "language" : "Java",
      "edition":"third",
      "author":"Heart Schildt",
      "history":
      [
          {
              "date":"2021-07-19",
              "item":"iphone"
          },
           {
              "date":"2021-07-30",
              "item":"android"
          }
      ]

 }
"""

#json.loads() : json형태의 데이터를 파이썬 딕셔너리 형태로 만들어 줌
json_data = json.loadS(data)

print(json_data['id'])
print(json_data['history'])
print(json_data['history'][0])
print(json_data['history'][0]['date'])