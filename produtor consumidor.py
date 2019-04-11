import time, random
import threading
#self.buffer[self.livre],se refere a uma lista,o self.livre,é um inteiro que indica a posição
#como usou o buffer que tava livre antes,na linha 18 o codigo soma o selv.livre + 1,pra ele apontar pra proxima posição ou próximo buffer
class Buffer:
  TAM_BUFFER = 5
  mutex  = threading.Semaphore(1)
  empty  = threading.Semaphore(TAM_BUFFER)
  full   = threading.Semaphore(0)
  buffer = list(range(TAM_BUFFER))
  cheio  = 0
  livre  = 0
  
  def inserir(self, item):
    self.empty.acquire()
    self.mutex.acquire()
    self.buffer[self.livre] = item
    self.livre = (self.livre + 1) % self.TAM_BUFFER
    self.mutex.release()
    self.full.release()

  def remover(self):
    self.full.acquire()
    self.mutex.acquire()
    item = self.buffer[self.cheio]
    self.cheio = (self.cheio + 1) % self.TAM_BUFFER
    self.mutex.release()
    self.empty.release()
    return item

b = Buffer()

def produtor():
  while True:
    time.sleep(random.randint(1, 10) / 100.0)
    item = random.randint(1, 10)
    b.inserir(item)
    print ("Produtor produziu:", item, b.livre, b.cheio)
    print (b.buffer)
    input()

def consumidor():
  while True:
    time.sleep(random.randint(1, 10) / 100.0)
    item = b.remover()
    print ("Consumidor consumiu:", item, b.livre, b.cheio)
    print(b.buffer)
    input()
    
A=threading.Thread(target=produtor,args=())
A.start()
B=threading.Thread(target=consumidor,args=())
B.start()

while 1: pass