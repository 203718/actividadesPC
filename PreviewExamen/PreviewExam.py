#Gerson Efher López Alvarez
import requests
from threading import Thread
import time
from weakref import finalize
import threading

urls = ["https://www.mapcrunch.com", "https://earth.google.com", 
        "https://quickdraw.withgoogle.com", "https://screamintothevoid.com", 
        "https://www.youtube.com", "https://mail.google.com/", 
        "https://www.canva.com", "https://www.facebook.com", 
        "https://www.netflix.com", "https://slidesgo.com", 
        "https://www.disneyplus.com/", "https://www.primevideo.com", 
        "https://account.live.com", "https://www.riotgames.com", 
        "https://www.epicgames.com", "https://store.steampowered.com", 
        "https://www.dominos.com", "https://play.hbomax.com", 
        "https://www.crunchyroll.com", "https://www.funimation.com", 
        "https://web.whatsapp.com", "https://order.kfc.com", 
        "https://www.amazon.com", "https://www.mercadolibre.com/", 
        "https://es.aliexpress.com/"]



def check_page(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            time.sleep(4)
            response = requests.head(url)
            if response.status_code == 200:
                print(f"{url} no disponible")
            else:
                print(f"{url} disponible")
        else:
            print(f"{url} no disponible")
    except:
        print(f"{url} disponible")      


class Hilo(threading.Thread):
    def __init__(self, id,url):
        threading.Thread.__init__(self)
        self.url=url

    def run(self):
        check_page(self.url)

x=0
urls = ["https://www.mapcrunch.com", "https://earth.google.com"]
y=1

while True:
    for x in urls:
        hilito= Hilo(y,x)
        hilito.start()
        y=y+1
    time.sleep(15)

print(f'Proceso ejecutado en {time_end - time_start}')