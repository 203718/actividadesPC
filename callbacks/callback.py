#CALLBACK
import threading
import requests

def get_service_1(response_json_data):
    print(response_json_data)

def get_error_1():
     print('Error en la solicitud')

def get_service_2(response_json_data):
    print(response_json_data)

def get_error_2():
     print('Error en la solicitud')

def request_data(url, succes_callback, error_callback):
    print("request_data")
    response= requests.get(url)
    if response.status_code == 200:
        succes_callback(response.json())
    else:
        error_callback()

class Hilo(threading.Thread):
    def _init_(self):
        threading.Thread._init_(self)

    def run(self):
        h1 = threading.Thread(target=request_data, 
        kwargs={
            'url':'http://3.22.27.8:3000/api/comprador/getAll',
            'succes_callback': get_service_1,
            'error_callback': get_error_1
        })
        h1.start

        h2 = threading.Thread(target=request_data, 
        kwargs={
            'url':'http://3.22.27.8:3000/api/controlEntregas/getAll',
            'succes_callback': get_service_2,
            'error_callback': get_error_2
        })
        h2.start


hilo= Hilo()
hilo.start