#debes de instalarte tweepy (pip install tweepy), (pip install tweepy[async]) =￣ω￣=

import tweepy
import time
import datetime
from time import sleep

 #pon tus tokens aqui =)
 #para solicitar los tokens debes entrar en Twitter Developers
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)

try: 
    api.verify_credentials()
    print("[+] Autenticación exitosa")
except:
    print("[-] Error al iniciar")
 
def publicar_tuip(message):
    api.update_status(status=message)
 
while True:
    now = datetime.datetime.now()
    h = now.hour    
    m = now.minute
    #aqui pones la hora y el minuto al que quieres que se tuitee
    if now.hour == 14:
        if now.minute == 30:
    #aqui pones que quieres tuitear ^^
            try:
                    publicar_tuip('Que coméis hoy?')
                    sleep(60)
            except:
                print("algo anda mal")
    sleep(2)