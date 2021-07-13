import requests

# s = requests.Session() ~ s.close()

with requests.Session() as s:
    param = {"name":"hong"}

    r = s.get("https://httpbin.org/get",params = param)
    print(r.headers)
    print(r.text)
    
