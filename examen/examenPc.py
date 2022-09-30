from threading import Lock
import time
from threading import Thread

lock = Lock()


def take(id):
    lock.acquire()
    print(f"El comensal {id+1} tiene los palillos")
    
def lower(id):
    lock.release()
    print(f"El comensal {id+1} solto los palillos")

def eat(id):
    print(f"El comensal {id+1} esta comiendo")
    time.sleep(3)
    print(f"El comensal {id+1} ha dejado comer")
    time.sleep(3)


class Persona(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        take(self.id)
        eat(self.id)
        lower(self.id)

for i in range(8):
    p=Persona(i)
    p.start()
