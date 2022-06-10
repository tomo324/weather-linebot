def rain_judge():
    from operator import truediv
    import requests
    res = requests.get('https://weather.tsukumijima.net/api/forecast?city=110010')
    res_json = res.json()
    forecasts = res_json['forecasts'][0]
    info = forecasts['dateLabel'] + ':' + forecasts['detail']['weather']
    weather = info.find('雨')
    
    if weather >= 0:
        return info , '傘を持っていきましょう！'
    else:
<<<<<<< HEAD
        return '傘は不要です！'
=======
        return info , '今日は雨は降らなさそうです！'
>>>>>>> 75c5cf610d8626a7797871f2f246d7cd72a0c8d1
