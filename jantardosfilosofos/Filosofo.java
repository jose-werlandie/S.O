package jantardosfilosofos;

/**
 *
 * @author werlan
 */
public class Filosofo extends Thread {
    int id;
    /**
     * estado
     */
    
    final int PENSANDO = 0;
    final int FAMINTO = 1;
    final int COMENDO = 2;
    
    public Filosofo(String nome, int id) {
        super(nome);
        this.id = id;
    }
    /**
     * Metodo Comfome.
     * informa qual filosofo está FAMINTO.
     */
    public void ComFome(){
        JantarDosFilosofos.estado[this.id] = 1;
        System.out.println("O Filosofo " + getName() + "está FAMINTO!");
    }
    /**
     * Metodo Come.
     * informa qual filosofo está COMENDO.
     */
    public void Come() {
        JantarDosFilosofos.estado[this.id]=2;
        System.out.println("O Filosofo  " +getName() + " está COMENDO" );
        try { 
            Thread.sleep(1000L);
        }catch ( InterruptedException ex){
            System.out.println("ERROR >" + ex.getMessage());
        }
    }
    /**
     * Metodo Pensa.
     * informaqaul Filosofo está PENSANDO.
     */
    public void Pensa() {
        JantarDosFilosofos.estado[this.id]=0;
        System.out.println("O Filosofo " + getName() + " está PENSANDO");
        try {
            Thread.sleep(1000L);
        }catch(InterruptedException ex){
            System.out.println("ERROR >" + ex.getMessage());
        }
    }
    /**
     * Metodo largarGarfo.
     * Quando um filosofo largar os garfos, o vizinho da esquerda e da direita podem tentar pegar os garfos.
     */
    
    public void LargarGarfo() throws InterruptedException {
        JantarDosFilosofos.mutex.acquire();
        Pensa();
        
        JantarDosFilosofos.filosofos[VizinhoEsquerda()].TentarObterGarfos();
        JantarDosFilosofos.filosofos[VizinhoDireita()].TentarObterGarfos();
        JantarDosFilosofos.mutex.release();
    }
    /**
     * Metodo PegarGarfo.
     */
    
    public void PegarGarfo () throws InterruptedException {
        JantarDosFilosofos.mutex.acquire();
        ComFome();
        /**
         * Condição for verdade,semaforo(1),permitir que o filosofo obtenha os garfos
         */
        TentarObterGarfos();
        JantarDosFilosofos.mutex.release();
        /**
         * condição não verdadeira,o filosofo vair ficar bloqueado
         * no seu indice de semaforo,até que possa tentar novamente
         */
        JantarDosFilosofos.semaforos[this.id].acquire();
        /**
         * semaforos[this.id] =new Semaphore (0).
         */
    }
    /**
     * Metodo TentarObterGarfos.
     * se o filosofo estiver faminto e o vizinho esquerda e direito não estiverem comendo,chama metodo come();
     */
    public void TentarObterGarfos() {
        if (JantarDosFilosofos.estado[this.id] == 1  
            && JantarDosFilosofos.estado[VizinhoEsquerda()] != 2 
            && JantarDosFilosofos.estado[VizinhoDireita()] != 2 ){
            Come();
            JantarDosFilosofos.semaforos[this.id].release();
            /**
             * semaforos[this.id] = new Semaphore(1)
             */
        }else{
            System.out.println(getName() + " não conseguiu comer!");
        } 
    }
    
    @Override
    public void run() {
        try {
            Pensa ();
            System.out.println("");
        do {
            PegarGarfo();
            Thread.sleep(1000L);
            LargarGarfo();
            }while (true);
        }catch(InterruptedException ex) {
            System.out.println("ERROR > " + ex.getMessage());
            return;
        }
    }
    
    public int VizinhoDireita() {
        return (this.id + 1) % 5;
    }
    
    public int VizinhoEsquerda(){
        if (this.id == 0){
            return 4;
        }else {
            return (this.id -1)% 5;
        }
    }
}
