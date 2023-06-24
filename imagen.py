
import present

class Imagen():
    imagen_normal_encriptar=""
    imagen_encriptada=""
    imagen_normal_desencriptar=""
    imagen_desencriptada=""

    def __init__(self):
        imagen_normal=""

    def encriptar_imagen(self):
        self.imagen_encriptada = present.encriptar_imagen(self.imagen_normal_encriptar)
        self.imagen_normal_desencriptar = self.imagen_encriptada

    def desencriptar_imagen(self):
        self.imagen_desencriptada = present.desencriptar_imagen(self.imagen_normal_desencriptar)

    def get_img_encriptada(self):
        return self.imagen_encriptada

    def get_img_desencriptada(self):
        return self.imagen_desencriptada
    
    def get_img_normal_encriptar(self):
        return self.imagen_normal_encriptar
    
    def get_img_normal_desencriptar(self):
        return self.imagen_normal_desencriptar
    
    def set_img_encriptar(self,path):
        self.imagen_normal_encriptar = path
    
    def set_img_desencriptar(self,path):
        self.imagen_normal_desencriptar = path
    
    

