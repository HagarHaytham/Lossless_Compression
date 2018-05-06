import decompressLZW



encodedMessage='files//encoded_1.tsv'
decodedMessage='files//decoded_1.tsv'

decode = decompressLZW.DecompressLZW(encodedMessage,decodedMessage)