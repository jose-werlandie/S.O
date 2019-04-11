import threading
import time, random
from threading import Thread

TAM = 5
garfos = []

for i in range (TAM):
	
	garfos.append(threading.Semaphore(1))

def Filosofo (f):
  f =int(f)
  while True:
    
    garfos[f].acquire()           # garfo da esquerda
    garfos[(f + 1) % 5].acquire() # garfo da direita
    print ("Filósofo", f, "comendo...")
	  
    time.sleep(random.randint(1, 5))
    
    garfos[f].release()
    garfos[(f + 1) % 5].release()
    print ("Filósofo", f, "pensando...")
	  
    time.sleep(random.randint(1, 10))

threads = []

for i in range(TAM):
   print ("Filósofo", i)
   threads.append(Thread(target=Filosofo, args=[i]))
   threads[i].start()
   
while 1: pass