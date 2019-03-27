#!/bin/bash -       
#title           :install-gp2009tr.sh
#description     :This script will install the gp2009tr python script for you
#author		 	     :Joep, PD1AEF
#date            :20190327
#version         :0.1   
#usage		       :bash install-gp2009tr.sh
#notes           :Based on the nice work by Raffaello, IZ0QWM

wget https://github.com/iz0qwm/gp2009tr/archive/master.zip
unzip master.zip
rm master.zip
cd gp2009tr-master/
sudo apt install python-pip
pip install websocket websocket-client configparser 


