# gp2009tr
Interface GP2009TR Pocsag transmitter for DAPNET

## Requisiti
- Trasmettitore GP2009TR http://www.witoptech.com/product-detail/pager-transmitter-pager-repeater/
- Software Windows in dotazione **Goupin Pager Message Transmitter Server system**
- Software Unipager 

## Funzionamento
Il software se vede un file nella cartella __Work__ formattato in questo modo:

 
        nome: call00.txt
        
        ADDRESS
        0220124
        Testo del messaggio

Invierà un messaggio al RIC 0220124 contenente "Testo del messaggio"  
Lo script gp2009tr.py legge via websocket i messaggi da un Unipager e crea il file per il software

## Installazione 
- Installare il software _Goupin_ su una macchina Windows e collegare il trasmettitore GP2009TR
- Installare il software Unipager e selezionare l'interfaccia Dummy
- Modificare il file gp2009tr.cfg in modo da puntare alle giuste directory ed in particolare alla directory Work del
software Windows (share di SAMBA e shared folder di VmWare se Unipager gira su un Debian sotto VmWare)
- Eseguire ./gp2009tr.py & (o eseguirlo come servizio)
