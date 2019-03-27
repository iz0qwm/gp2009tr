# gp2009tr
Interface GP2009TR Pocsag transmitter for DAPNET

## Requirements
- Transmitter GP2009TR http://www.witoptech.com/product-detail/pager-transmitter-pager-repeater/
- Windows Software from GP2009TR **Goupin Pager Message Transmitter Server system**
- Unipager Software 

## Running
The software looks for a file in the directory __Work__ formatted like this:

 
        name: call00.txt
        
        ADDRESS
        0220124
        Text of the message

The software will send a message to the RIC 0220124 containing "Text of the message"  
The script gp2009tr.py reads via websocket the messages coming from Unipager and creates the file for the software

## Installation 
- Install the software _Goupin_ on a Windows and connect the transmitter GP2009TR
- Install the software Unipager and select the Dummy interface
- Modify the file gp2009tr.cfg configuring the right directories and pay attention that Work is the directory shared by
Windows (SAMBA share or VMWare shared folder if Unipager runs on Debian under VmWare)
- Run ./gp2009tr.py & (or run like service)
