import threading
import time, random

class BufferLimitado:                               #Cria classe BufferLimitado
  TAM_BUFFER = 5		                            #Atribui 5 a variavel criada TAM_BUFFER
  mutex  = threading.Semaphore(1)                   #Cria variavel mutex e atribui a ela o objeto threading.Semaphore() com valor 1
  empty  = threading.Semaphore(TAM_BUFFER)          #Cria variavel empty e atribui a ela o objeto threading.Semaphore() com valor do buffer
  full   = threading.Semaphore(0)  	                #Cria variavel full e atribui a ela o objeto threading.Semaphore() com valor 0
  buffer = list(range(TAM_BUFFER))                  #Cria variavel buffer uma lista para elementos tamanho = buffer
  cheio  = 0                                        #Cria variavel cheio e atribui 0
  livre  = 0	                                    #Cria variavel livre e atribui 0
  
  def inserir(self, item):                          #Define metodo/funcao inserir que recebe parametro/argumento item
    self.empty.acquire()                            #Chama metodo acquire do objeto threading.Semaphore() atribuido a variavel empty
    self.mutex.acquire()                            #Chama metodo acquire do objeto threading.Semaphore() atribuido a variavel mutex
    self.buffer[self.livre] = item                  #Atribui item ( recebido atravez da chamada da funcao/metodo) ao indice 0(zero) da lista buffer
    self.livre = (self.livre + 1) % self.TAM_BUFFER #Incrementa a variavel livre definida no inicio do codigo como 0(zero) para 1 (livre+1 modulo buffer)." Resto da divisao de (0+1)%5 = 1"
    self.mutex.release()                            #Chama metodo release do objeto threading.Semaphore() atribuido a variavel mutex
    self.full.release()                             #Chama metodo release do objeto threading.Semaphore() atribuido a variavel full

  def remover(self):                                #Define metodo/funcao remover que nao recebe parametro/argumento
    self.full.acquire()                             #Chama metodo acquire do objeto threading.Semaphore() atribuido a variavel full
    self.mutex.acquire()                            #Chama metodo acquire do objeto threading.Semaphore() atribuido a variavel mutex
    item = self.buffer[self.cheio]                  #Atribui a item o elemento no indice 0 da lista
    self.cheio = (self.cheio + 1) % self.TAM_BUFFER #Incrementa a variavel cheio, definida no inicio do codigo como 0(zero), para 1 (cheio+1 modulo buffer)." Resto da divisao de (0+1)%5 = 1"
    self.mutex.release()                            #Chama metodo release do objeto threading.Semaphore() atribuido a variavel mutex
    self.empty.release()                            #Chama metodo release do objeto threading.Semaphore() atribuido a variavel empty
    return item                                     #Retorna o elemento atribuido a indice cheio da lista que na primeira chamada era 0

b = BufferLimitado()                                # atribui a b a classe BufferLimitado

def produtor():
  while True:
    time.sleep(random.randint(1, 10) / 100.0)            #chama metodo sleep do modulo time
    item = random.randint(1, 10)                         #Atribui a item o retorno do metodo random.randint " limitando em valores inteiros de 1 a 10"
    b.inserir(item)                                      #Chama metodo inserir da classe BufferLimitado com argumento item.
    print ("Produtor produziu:", item, b.livre, b.cheio) #imprime item, o valor em livre, e o valor em cheio

def consumidor():
  while True:
    time.sleep(random.randint(1, 10) / 100.0)              #chama metodo sleep do modulo time
    item = b.remover()                                     #Chama metodo remover da classe BufferLimitado atribuindo a item o valor de retorno.
    print ("Consumidor consumiu:", item, b.livre, b.cheio) #imprime item, o valor em livre, e o valor em cheio

A=threading.Thread(target=produtor,args=())
A.start()
B=threading.Thread(target=consumidor,args=())
B.start()

while 1: pass

#O codigo simula o comportamento consumidor produtor com uso de semafhoros, 
#para garantir que o buffer será usado,uso o modolulo time, para que hora Produtor seja mais rapido que o consumidor consome,
#ou consumidor consuma mais que o produtor seja capaz de produzir. 