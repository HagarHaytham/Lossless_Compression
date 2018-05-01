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
        self.left=self.right=None#dah el null , mafeesh pointers ,let's just try
        #should i put left and right here ,, or implement a new class called Node ????
        
    #operator overloading of less than operator    
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    #operator overloading for printing symbol
    def __str__(self):
        return "Value:" + str(self.value) +" Frequency:"+str(self.frequency)+ " Probability:"+str(self.probability)
    
    
#s=Symbol('h',10,0.1)
#s1=Symbol('m',5,0.05)
#print(s<s1)
#print(s)