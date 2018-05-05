# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:54 2018

@author: hagar
"""

import encoder
#import huffman
#import decoder

# from encoder import encoder as en
#import sys
#print (sys.path)



inputFile='files//DataSet_5.tsv'
#inputFile1='files//t2.tsv'
encodedMessage='encoding//encoded_5.tsv'
codeTable='codetables//codetable_5.tsv'
decodedMessage='decoding//output_1.tsv'

encoder1=encoder.Encoder(inputFile)
encoder1.Encode(codeTable,encodedMessage)

#Huffman1.printCodeTable(codeTable)

#huffman1=encoder1.Encode(codeTable,encodedMessage)

#el decoder ya5od file el codetable w yconstuct huffman tree
#w ba3d keda y decode el file