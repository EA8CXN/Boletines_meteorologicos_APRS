#!/usr/bin/python3
import sys
import requests
import feedparser

i = 0
while i < 5:
    #DEPURAR PAYLOAD
    def clean_data(input):
        inputs  = ["Á","É","Í","Ó","Ñ","Ü","á","é","í","ó","ú",]
        outputs = ["A","E","I","O","N","U","a","e","i","o","u",]
        y = len(inputs)
        for x in range(y):
            input = input.replace(inputs[x].decode('utf8'),outputs[x])
            return(input)

    #Adquirir datos RSS
    d = feedparser.parse('http://www.aemet.es/documentos_d/eltiempo/prediccion/avisos/rss/CAP_AFAZ659601_ATOM.xml')
    Payload = (d.entries[i].title)
    if Payload =="Estado completo de avisos para Norte de Tenerife. No hay avisos para Norte de Tenerife":
        Payload = "NIVEL VERDE: SIN AVISOS AEMET / NO METEOROLOGICAL WARNINGS"
    
    
    #IMPRIMIR A ARCHIVO
    f = open('/home/pi/Boletines/boletin'+str(i)+'.txt' , 'w')
    print(':BLN'+str(i)+'     :', file=f, end='')
    print(Payload, file=f)
    f.close()
    i = i + 1
