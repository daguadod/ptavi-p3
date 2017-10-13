#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler  import SmallSMILHandler

if __name__ == "__main__":

    try:
        file = sys.argv[1]
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(file))
        lista = sHandler.get_tags()
        exit = ''
        for etiqueta in lista:
            names = etiqueta[0]
            valores = etiqueta[1]
            atributos = ''
            for attrs in valores:
                if valores[attrs] != '': 
                    atributos += '\t' + attrs + '="' + valores[attrs] + '"'
            exit += names  + atributos + '\n'
        print(exit)

    except IndexError: 
            sys.exit('Usage python3 karaoke.p file.smil')
