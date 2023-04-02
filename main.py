import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

import weather_search 


CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

umbrella = weather_search.rain_judge()

def main():
    USER_ID = os.environ.get('USER_ID')
    messages = TextSendMessage(text = umbrella[0]+ '\n' + '----------------------' + '\n' +  umbrella[1])
    line_bot_api.push_message(USER_ID,messages=messages)

if __name__ == "__main__":
    main()