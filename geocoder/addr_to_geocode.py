import requests, json

# http://api.vworld.kr/req/address?service=address&request=getCoord&key=인증키&[요청파라미터]
# key = 2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40
pkey = '2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40'
r = requests.get("http://api.vworld.kr/req/address?service=address&request=getCoord&key=2B78A4C2-7920-3DD9-9C3D-2BDB01FB6F40&&crs=epsg:4326&address=%EA%B5%AD%EC%B1%84%EB%B3%B4%EC%83%81%EB%A1%9C76%EA%B8%B8%2024&refine=true&format=json&type=ROAD")
data = r.json()
coordinate = data['response']['result']['point']
lat = coordinate['y']
long = coordinate['x']
print(lat, long)


