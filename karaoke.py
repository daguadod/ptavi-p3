#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

class KaraokeLocal:

    def __init__(self, file):
        
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(file))
        self.lista = sHandler.get_tags()

    def __str__(self):

        exit = ''
        for etiqueta in self.lista:
            names = etiqueta[0]
            valores = etiqueta[1]
            atributos = ''
            for attrs in valores:
                if valores[attrs] != '':
                    atributos += '\t' + attrs + '="' + valores[attrs] + '"'
            exit += names + atributos + '\n'

        return exit

    def to_json(self, fileSmil, fileJson=None):

        if fileJson == None:
            fileJson = fileSmil.replace('.smil', '.json')
        with open(fileJson, 'w') as outfile_json:
            json.dump(self.lista, outfile_json, indent=3, 
            separators=(' ', ': '))

    def do_local(self):

        for valores in self.lista:
            valor = valores[1]
            for attrs in valor:
                if attrs == 'src':
                    try:
                        url = valor[attrs].split('/')
                        urllib.request.urlretrieve(valor[attrs], url[-1])
                        valor[attrs] = url[-1]
                    except ValueError: 
                        pass
            

if __name__ == "__main__":

    try:
        file = sys.argv[1]
    except IndexError: 
            sys.exit('Usage python3 karaoke.p file.smil')
    karaoke = KaraokeLocal(file)
    print(karaoke)
    karaoke.to_json(file)
    karaoke.do_local()
    karaoke.to_json(file, "local.json")
    print(karaoke)
