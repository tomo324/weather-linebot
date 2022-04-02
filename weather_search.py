def rain_judge():
    from operator import truediv
    import requests
    res = requests.get('https://weather.tsukumijima.net/api/forecast?city=130010')
    res_json = res.json()
    forecasts = res_json['forecasts'][0]
    info = forecasts['dateLabel'] + ':' + forecasts['detail']['weather']
    weather = info.find('雨')
    
    if weather >= 0:
        return '傘を持っていきましょう！'
    else:
        return '今日は雨は降らなさそうです！'
