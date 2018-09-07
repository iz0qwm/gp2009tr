# gp2009tr
Interface GP2009TR Pocsag transmitter for DAPNET

## Requisiti
- Trasmettitore GP2009TR http://www.witoptech.com/product-detail/pager-transmitter-pager-repeater/
- Software Windows in dotazione **Goupin Pager Message Transmitter Server system**

## Funzionamento
Installare il software su una macchina Windows e collegare il trasmettitore.
Il software se vede un file nella cartella __Work__ formattato in questo modo:

 
        nome: call00.txt
        
        ADDRESS
        0220124
        Testo del messaggio

Invierà un messaggio al RIC 0220124 contenent "Testo del messaggio"

## Esecuzione dello script
