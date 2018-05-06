# -*- coding: utf-8 -*-


import compressLZW

#import binascii

class Encoder: 
    def __init__(self,inputfile,outputfile): #constructor in python
    #self must be passed to any method in the class
        self.inputFile=inputfile
        print('Encoder constructor')
        self.message=self.ReadFile()
        self.LZW=compressLZW.CompressLZW(self.message,outputfile)
        
        
        
    def ReadFile(self):# don't forget self to be passed to any method in the class !! please XD
        #read file as binary file (in the form of bytes)
        print('Encoder readfile')
        with open (self.inputFile,'rb') as rf:
            arr = bytearray(rf.read()) 
            return arr
# 