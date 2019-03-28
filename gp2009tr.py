#!/usr/bin/python
#title           :gp2009tr.py
#description     :This script will check for DAPNET messages and send it to the remote Work folder
#author		 :Raffaello, IZ0QWM
#date            :20180908
#version         :0.1   
#notes           :Translation of remarks by Joep, PD1AEF
import websocket
import json
import string
import re
import sys
import os
import requests
import logging
import configparser
from random import randint
import subprocess


# Read the configuration file
cfg = configparser.RawConfigParser()
try:
        #attempt to read the config file config.cfg
        config_file = os.path.join(os.path.dirname(__file__),'gp2009tr.cfg')
        cfg.read(config_file)
except:
        #no luck reading the config file, write error and bail out
        print(os.path.basename(__file__) + " could not find / read config file")
        sys.exit(0)

# Read location of the log file
logfile = cfg.get('misc', 'logfile')

#logging.basicConfig(filename='gp2009tr.log',level=logging.INFO) # level=10
logger = logging.getLogger('dapnet')
handler = logging.FileHandler(logfile)
logformat = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(logformat)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Read info from DAPNET
transmitterws = cfg.get('dapnet','transmitterws')
# Read info for messages to send
messagetx = cfg.get('misc','message')

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    json_message = json.loads(message)
    log_message = json_message['Log']
    string_message = str(log_message)
    if string_message.find("data") == -1:
        pass
    else:
        prev_mittente = "addr: "
        left,sep,right = string_message.partition(prev_mittente)
        destinatario_virgola = right[:7]
        destinatario = destinatario_virgola.split(',')[0]
        #print recepient RIC
        prima,messaggio = string_message.split('data:')
        #print message
        clean1_messaggio = messaggio.replace("\" }']", "")
        clean2_messaggio = clean1_messaggio.replace(" \"", "")
        #print clean1_message
        #print clean2_message
        #logger.info('gp2009tr_trx %s engaged...', version)
        #
        logger.info("RIC: %s - Messaggio: %s", destinatario, clean2_messaggio)
        file = open(messagetx,"w")
        file.write("ADDRESS\n")
        file.write(destinatario + "\n")
        file.write(clean2_messaggio + "\n")
        file.close()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
        string_to_send = "{\"GetStatus\"}"
        #ws.send("Hello %d" % i)
        ws.send(string_to_send)
        time.sleep(5)
        #ws.close()
        #print("thread terminating...")
        thread.start_new_thread(run, ())


if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp(transmitterws,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
