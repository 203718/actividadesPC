
from mimetypes import init
import threading
from tkinter import Y
from unicodedata import name
import requests
import time
import psycopg2
import concurrent.futures
import json
import pytube

#descargar 5 videos
#Escribir en base de datos por lo menos 2000 registros 
#Generar una solicitud a randomuser de por lo menos 50 usuarios   
def conect():
    conexion = psycopg2.connect(user='postgres', password='gerson', host='localhost', port='5432', database='registros')
    return conexion


def get_services():
    #time.sleep(0.5)
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name=results[0].get('name').get('first')
        print(name)


def get_services2():
    response = requests.get('https://randomuser.me/api/?results=2000')

    if response.status_code == 200:
        response_json=json.loads(response.text)
        for i in response_json['results']:
            namePerson = i ['name']['first']
            #print(name)
            write_db(namePerson)
        print('Datos registrados')


def write_db(x):
    dataNames = json.dumps(x)
    conn = conect()

    conexion2 = conn.cursor()
    conexion2.execute("insert into nombres(name) values(%s)",(dataNames,))
    conn.commit()
    conn.close()  




guardar = "D:/Downloads/pruebaVideo"
url = ["https://www.youtube.com/watch?v=I8c7UBa_0nk","https://www.youtube.com/watch?v=fHR1CZ9x61E","https://www.youtube.com/watch?v=sbLqX7cUKoM","https://www.youtube.com/watch?v=hoQmSA6MRAk","https://www.youtube.com/watch?v=sfQOiDJX-x4"]
threading_local = threading.local()

def get_services3():
    video0 = pytube.YouTube(url[0])
    video0.streams.first().download(guardar)

    video1 = pytube.YouTube(url[1])
    video1.streams.first().download(guardar)

    video2 = pytube.YouTube(url[2])
    video2.streams.first().download(guardar)

    video3 = pytube.YouTube(url[3])
    video3.streams.first().download(guardar)

    video4 = pytube.YouTube(url[4])
    video4.streams.first().download(guardar)




if __name__ =='__main__':
    init_time = time.time()
    #th2 = threading.Thread(target=get_services2)
    #th2.start()
    #th3 = threading.Thread(target=get_services3)
    #th3.start()
    for x in range(0,50):
        th1 = threading.Thread(target=get_services)        
        th1.start()
        th1.join()
    
    end_time = time.time() - init_time
    print(end_time)
        