import requests
import telepot
from tokens import *

class TelegramBot:
    def __init__(self) -> None:
        self.bot = telepot.Bot(TELEGRAM_TOKEN)


    def sendMessage(self, mensagem) -> None:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensagem}"
        print(requests.get(url))
        

    def sendPhoto(self, imagemLocal) -> None:
        photo = open(f'./images/{imagemLocal}', 'rb')
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto?chat_id={CHAT_ID}"
        print(requests.post(url, files={'photo': photo}))