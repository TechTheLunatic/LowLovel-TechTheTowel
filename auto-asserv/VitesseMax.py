# -*-coding:utf-8-*-
from serial import Serial, SerialTimeoutException, SerialException
from asserv2 import *
import matplotlib.pyplot as plt
import time


class serialCom:
    def __init__(self, serialPort):
        self.port = serialPort
        try:
            self.port_serie = Serial(port=self.port, baudrate=115200, timeout=0)
            print self.port_serie.isOpen()
        except SerialException:
            print "impossible d'ouvrir le port : " + str(serialPort)

    def ping(self):
        
        self.port_serie.write("?\r\n")
    
    def ecouter(self):
        #print "on lit"
        #a=self.port_serie.readline()    # Lit l'underscore (acquittement)
        a=self.port_serie.readline() 
        #print a
        return a

    def parler(self, a_envoyer):
        #raw_input("écrire ici")
        self.port_serie.write(a_envoyer)
        return a_envoyer

    def quitter(self):
        self.port_serie.close()
		
		



com=serialCom("COM5")
test=ShittyClass()

while(not test.done):
    serialCom.parler(com, "testSpeed\r\n")
    time.sleep(2)
    a=serialCom.ecouter(com)
    a=serialCom.ecouter(com)
    while(a!="endtest"):
        ShittyClass.doYourShit(test, a)
        a=serialCom.ecouter(com)
    ShittyClass.computeThatShit(test)
    print "MaxG"
    print test.maxG
    print "MaxD"
    print test.maxD
    
    

    ShittyClass.resetYourShit(test)
    
    raw_input("Waiting your shitty order")

    serialCom.parler(com, "kpg\r\n")
    serialCom.parler(com, str(test.KpG)+"\r\n")
    serialCom.parler(com, "kpd\r\n")
    serialCom.parler(com, str(test.KpD)+"\r\n")
    serialCom.parler(com, "testSpeedReverse\r\n")
    time.sleep(2)
    a=serialCom.ecouter(com)
    while(a!="endtest"):
        ShittyClass.doYourShit(test, a)
        a=serialCom.ecouter(com)
    ShittyClass.computeThatShit(test)
    print "MaxG"
    print test.maxG
    print "MaxD"
    print test.maxD

    ShittyClass.resetYourShit(test)

    raw_input("Waiting your shitty order")
