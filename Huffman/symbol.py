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