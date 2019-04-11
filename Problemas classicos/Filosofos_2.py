import threading
import time, random
from threading import Thread

s = threading.Lock()

def tempo(i):
   t = random.randint(1,6)
   print (" Filósofo",i, "pensando ")
   time.sleep(t)

def filosofo(i):

  while True :
    print(" Filosofo",i," pegando colher ")
    s.acquire()
    print (" Filósofo",i,"Comendo ")
    tempo(1)
    print (" Filósofo",i,"Liberando colher ")
    s.release()
    print (" Filósofo",i,"Faminto ")
    tempo(1)

threads = []

for i in range(5):
   print ("Filósofo", i)
   threads.append(Thread(target=filosofo, args=[i]))
   threads[i].start()
   
while 1: pass