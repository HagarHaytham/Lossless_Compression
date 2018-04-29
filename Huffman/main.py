# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:54 2018

@author: hagar
"""

import encoder
import huffman
import decoder
# from encoder import encoder as en
#import sys
#print (sys.path)



inputFile='DataSet_1.tsv'
encodedMessage='encoded.tsv'
codeTable='codetable.tsv'
decodedMessage='output.tsv'

encoder1=encoder.Encoder(inputFile)
#encoder1.GenerateSymbols()

#huffman1=encoder1.Encode(codeTable,encodedMessage)

#el decoder ya5od file el codetable w yconstuct huffman tree
#w ba3d keda y decode el file