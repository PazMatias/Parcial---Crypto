
class Present():

    permute = [0]*64  
    pbox_inv = [0]*64
    subkeys = []
    rounds = 32 
    sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2] 
    sbox_inv = []
    masterKey = 0 
    m = 0 
    encripted_message = 0

    def __init__(self):
        self.initPLayer()
        self.initPLayer_inv()
        self.initSbox_inv()

    def setKey(self, key):
        if(len(key)*4 == 80 or len(key)*4 == 128):  
            temp_key = bytes.fromhex(key)  
            self.masterKey = int.from_bytes(temp_key, byteorder='big')  
            if((len(key)*4) == 80):
                self.subKeys80()  
            else:
                self.subKeys128()
        else:
            print('Length of key must be either 80 bits or 128 bits')
            exit()

    def setMessage(self, message):
        self.m = int(message, 16)

    def initPLayer(self):
        c = -1
        for i in range(64):
            if ((16*i) % 64) == 0:
                c += 1
            self.permute[i] = (16*i) % 64 + c

    def initPLayer_inv(self):
        self.pbox_inv = [self.permute.index(x) for x in range(64)]

    def initSbox_inv(self):
        index_inv = [self.sbox.index(x) for x in range(len(self.sbox))]
        self.sbox_inv = index_inv
        

    def subKeys80(self):
        for i in range(1, self.rounds+1):  
            self.subkeys.append(self.masterKey >> 16)  

            self.masterKey = ((self.masterKey & (2**19 - 1)) << 61) | (self.masterKey >> 19)

            self.masterKey = ((self.sbox[self.masterKey >> 76] << 76) | self.masterKey & (2**76 - 1))

            self.masterKey = (self.masterKey ^ (i << 15))

    def subKeys128(self):
        for i in range(1, self.rounds+1):  
            self.subkeys.append(self.masterKey >> 64)  

            self.masterKey = (((self.masterKey & (2**67 - 1)) << 61) | (self.masterKey >> 67))

            out1 = (self.sbox[self.masterKey >> 124] << 124)  
            out2 = (self.sbox[(self.masterKey >> 120) & 15] << 120)  
            out3 = (self.masterKey & (2**120 - 1)) 
            self.masterKey = (out1 | out2 | out3)

            self.masterKey = (self.masterKey ^ (i << 62))

    def pLayer(self, state):
        res = 0
        for i in range(64):  
            bit = ((state >> i) & 1)  
            res = (res | (bit << self.permute[i]))
        return res
    
    def pLayer_inv(self, state):
        res = 0
        for i in range(64):  
            bit = ((state >> i) & 1)  
            res = (res | (bit << self.pbox_inv[i]))
        return res
    
    def addRoundKey(self, state, subkey):
        return (state ^ subkey)

    def sBoxLayer(self, state):
        res = 0
        for i in range(16):  
            bits = ((state >> (i*4)) & (2**4 - 1))
            res += (self.sbox[bits] << (i*4))
        return res
    
    def sBoxLayer_a(self, state):
        res = 0
        for i in range(16): 
            bits = ((state >> (i*4)) & (2**4 - 1))
            res += (self.sbox[bits] << (i*4))
        return res

    def sBoxLayer_inv(self, state):
        res = 0
        for i in range(16):  
            bits = ((state >> (i*4)) & (2**4 - 1))
            res += (self.sbox_inv[bits] << (i*4))
        return res

    def encryption(self):
        state = self.m
        for i in range(self.rounds-1):
            state = self.addRoundKey(state, self.subkeys[i])
            state = self.sBoxLayer(state)
            state = self.pLayer(state)

        state = self.addRoundKey(state, self.subkeys[-1])
        self.encripted_message = state

        result = hex(state).replace('0x', '')
        if len(result) < 16:
            result=result.zfill(16)
        return result


    def desencryption(self):
        state = self.m
        for i in range(self.rounds - 1):
            state = self.addRoundKey(state, self.subkeys[ -i -1])
            state = self.pLayer_inv(state)
            state = self.sBoxLayer_inv(state)
        state = self.addRoundKey(state, self.subkeys[0])


        result = hex(state).replace('0x', '')
        if len(result) < 16:
            result=result.zfill(16)
        return result

