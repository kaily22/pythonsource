from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org/"

#url = api + "?" + "format=json"

values = {"format":"text"}

url = api + "?" + urlencode(values)

print("요청 url ",url)

response = urlopen(url).read().decode("utf-8")
print(response)

