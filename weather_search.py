import requests
res = requests.get('https://weather.tsukumijima.net/api/forecast?city=130010')
res_json = res.json()
forecasts = res_json['forecasts'][0]
info = forecasts['dateLabel'] + ':' + forecasts['detail']['weather']
weather = info.find('雨')

#雨予報か判定
if weather > 0:
    print('傘を持っていきましょう！')
else:
    print(None)

print(info)
print(weather)
