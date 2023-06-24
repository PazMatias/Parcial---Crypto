from algorithm import Present
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

# """
# print("Enter 8 Characters")
# msg_str = input()
# print("Enter key in hex, 20 hex characters for 80bit  or 32 hex characters for 128bit")
# key_hex_str = input()
# """

def encriptar_imagen(path):
    key_hex_str = "ABC11234A8DA9D123FABD223123313AB"
    img2 = Image.open(path,mode='r').convert('L')
    img2 = img2.resize((400,400))
    img_bytes = np.asarray(img2)
    img_bytes = img_bytes.flatten()
    list_bytes = []
    list_encript = []
    cipher = Present()
    cipher.setKey(key_hex_str)
    index = 0
    for i in range(0,len(img_bytes)):
        list_bytes.append(img_bytes[i])
        if index == 7:
            img_hex = bytes(list_bytes).hex()
            cipher.setMessage(img_hex)
            encript=cipher.encryption()
            list_encript.append(np.frombuffer(bytes.fromhex(encript), dtype='uint8'))
            index = 0
            list_bytes = []
        else:
            index += 1
    imag_encript = np.resize(list_encript,(400,400))
    imag_encript = np.asarray(imag_encript,dtype='uint8')

    img2 = Image.fromarray(imag_encript)
    img2.save('ImagenEncriptada.png')
    img2.close()
    return "./ImagenEncriptada.png"

def desencriptar_imagen(path):
    key_hex_str = "ABC11234A8DA9D123FABD223123313AB"
    img2 = Image.open(path,mode='r').convert('L')
    img_bytes = np.asarray(img2)
    img_bytes = img_bytes.flatten()
    list_bytes = []
    list_encript = []
    cipher = Present()
    cipher.setKey(key_hex_str)
    index = 0
    for i in range(0,len(img_bytes)):
        list_bytes.append(img_bytes[i])
        if index == 7:
            img_hex = bytes(list_bytes).hex()
            cipher.setMessage(img_hex)
            encript=cipher.desencryption()
            list_encript.append(np.frombuffer(bytes.fromhex(encript), dtype='uint8'))
            index = 0
            list_bytes = []
        else:
            index += 1
    imag_encript = np.resize(list_encript,(400,400))
    imag_encript = np.asarray(imag_encript,dtype='uint8')
    img2 = Image.fromarray(imag_encript)
    img2.save('ImagenDesencriptada.png')
    img2.close()
    return "./ImagenDesencriptada.png"
