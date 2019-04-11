package jantardosfilosofos;

import java.util.concurrent.Semaphore;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author werlan
 */
public class JantarDosFilosofos {

    /**
     * 
     * classe principal. 
     */
    static Semaphore mutex = new Semaphore(1); 
    //Cria variavel estatica mutex e atribui a ela o objeto Semaphore() com valor 1
    static Semaphore[] semaforos = new Semaphore[5];
    
    static Filosofo[] filosofos = new Filosofo[5];
    
    static int[] estado = new int[5];
    
    /**
     * 
     * main principal 
     */
    public static void main(String[] args){
        /**
         * todos os filosofos começam pensando
         */
        for (int i =0; i< estado.length;  i++){
            estado[i]= 0;
        }
        //inicializa todos filosofos
        filosofos[0] = new Filosofo ("platao",0);
        filosofos[1] = new Filosofo ("Socratis",1);
        filosofos[2] = new Filosofo ("Aristotoles",2);
        filosofos[3] = new Filosofo ("tales",3);
        filosofos[4] = new Filosofo ("parmenides",4);
        
        /**
         * definir posse dos garfos.
         */
        for (int i = 0; i < filosofos.length; i++){
            System.out.println("garfo " + i + " - filosofo " + i + " - garfo " + (i + 1) %5);
        }
        System.out.println("");
        
        for (int i = 0; i < semaforos.length; i++){
            semaforos[i] = new Semaphore(0);
        }
        
        for (int i = 0; i < filosofos.length; i++){
            filosofos[i].start();
        }
        /**
         * execução limitada em 20 segundos.
         */
        try {
            Thread.sleep(20000);
            System.exit(0);
        }catch ( InterruptedException ex){
            Logger.getLogger(JantarDosFilosofos.class.getName()).log(Level.SEVERE,null,ex);
        }
    }
}