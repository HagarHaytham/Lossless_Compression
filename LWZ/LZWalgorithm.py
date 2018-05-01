# -*- coding: utf-8 -*-
def encodeLzw(input_string):
	for char in input_string:
		if char in dictionary:	
			continue
		else:
			dictionary.append(char)
	dictionary.sort()
	#no_input = len(dictionary)
	next = ""
	for char in input_string:
		a = next + char
		if a in dictionary:
			next = a
		else:
			next = a[len(a)-1]
			dictionary_word = a[0:len(a)-1]	
			dictionary.append(a)
			encoded_version.append(dictionary.index(dictionary_word))
	encoded_version.append(dictionary.index(next))

def decodeLzw( encoded_version ):
	x = ""	
	for i in encoded_version:
		x = x + dictionary[i]
	return x

dictionary = []
encoded_version = []
encodeLzw("عم يا صياد")
print(dictionary)
decoded_version = decodeLzw(encoded_version)
print("The encoded version of the given string is: ", encoded_version)
print("The Decoded version of the encoded string is: ",decoded_version)
