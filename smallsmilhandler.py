#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    # Clase para archivos Smill
    def __init__ (self):
        
        self.List = []
        self.root_layout = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}

    def startElement(self, name, attrs):
    # Abrir etiquetas
        if name == 'root_layout':
            self.root_layout['width'] = attrs.get("width","") 
            self.root_layout['height'] = attrs.get("height","")
            self.root_layout['background-color'] = attrs.get("background-color"
                                                    ,"") 
            self.List.append(self.root_layout)
            print("root_layout:", self.List[0])
            

        if name == 'region':
            self.region['id'] = attrs.get('id', "")
            self.region['top'] = attrs.get('top', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('left', "")
            self.region['right'] = attrs.get('right', "")
            self.List.append(self.region)
            print("region:", self.List[1])

        if name == 'img':
            self.img['src'] = attrs.get("src","") 
            self.img['region'] = attrs.get("region","")
            self.img['begin'] = attrs.get("begin","") 
            self.img['dur'] = attrs.get("dur","")
            self.List.append(self.img)
            print("img", self.List[2])

        if name == 'audio':
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['dur'] = attrs.get('dur', "")
            self.List.append(self.audio)
            print("audio", self.List[3])

        if name == 'textstream':
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            self.List.append(self.textstream)
            print("texstream", self.List[4])

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
