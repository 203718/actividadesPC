import threading 
from time import sleep

mutex = threading.Lock()

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        sleep(3-self.id)
        print("valor"+str(self.id))
        mutex.release

    def crito(id):
    global
