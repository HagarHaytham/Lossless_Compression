# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 00:20:21 2018

@author: hagar
"""
#i think mafeesh structs f python
class Symbol:
    def __init__(self,val,frequency,probability):
        self.value=val #byte
        self.frequency=frequency #number of occuraces in the message
        self.probability=probability #frequency/size
        
        
    #operator overloading of less than operator    
    def __lt__(self, other):
        return self.frequency<other.frequency
    
    #operator overloading for printing symbol
    def __str__(self):
        return "Value:" + str(self.value) +" Frequency:"+str(self.frequency)+ " Probability:"+str(self.probability)
    