from algorithm import Present    
#from present_2 import Present
from binascii import hexlify,unhexlify
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

# """
# print("Enter 8 Characters")
# msg_str = input()
# print("Enter key in hex, 20 hex characters for 80bit  or 32 hex characters for 128bit")
# key_hex_str = input()
# """

key_hex_str = "ABC11234A8DA9D123FABD223123313AB"
plain = "ff0c84050b20414b"

chiper = Present()
chiper.setKey(key_hex_str)
chiper.setMessage(plain)
encripted_text = chiper.encryption()
print(encripted_text)
#decripted_text = chiper.desencryptation()
#print(decripted_text)
