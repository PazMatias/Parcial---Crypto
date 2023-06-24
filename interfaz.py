import tkinter
from tkinter.filedialog import askopenfilename
import customtkinter
from imagen import Imagen
from PIL import Image

imagen = Imagen()
label_array = [0]*4


def agregar_imagen(path,tab,px,py,index):
    my_image = customtkinter.CTkImage(dark_image=Image.open(path,mode='r').convert('L'),size=(400, 400))
    my_image_lb = customtkinter.CTkLabel(master=tabview.tab(tab),image=my_image ,text="")
    my_image_lb.place(x=px,y=py)
    label_array[index]=my_image_lb

def cargar_imagen_a_encriptar():
    filename = askopenfilename()
    imagen.set_img_encriptar(filename)
    agregar_imagen(imagen.get_img_normal_encriptar(),"Encriptar",250,0,0)
    
def cargar_imagen_a_desencriptar():
    filename = askopenfilename()
    imagen.set_img_desencriptar(filename)
    agregar_imagen(imagen.get_img_normal_desencriptar(),"Desencriptar",250,0,2)
    
def limpiar_imagenes_encriptar():
    if imagen.get_img_normal_encriptar() != "" and imagen.get_img_encriptada() != "":
        for i in range(2):
            label_array[i].destroy()

def limpiar_imagenes_desencriptar():
    if imagen.get_img_normal_desencriptar != "" and imagen.get_img_desencriptada() != "":
        for i in range(2,4):
            label_array[i].destroy()

def encriptar():
    if imagen.get_img_normal_encriptar() != "":
        imagen.encriptar_imagen()
        agregar_imagen(imagen.get_img_encriptada(),"Encriptar",700,0,1)
        agregar_imagen(imagen.get_img_encriptada(),"Desencriptar",250,0,2)

def desencriptar():
    if imagen.get_img_normal_desencriptar() != "":
        imagen.desencriptar_imagen()
        agregar_imagen(imagen.get_img_desencriptada(),"Desencriptar",700,0,3)


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
wdth = app.winfo_screenwidth()
hgt = app.winfo_screenheight()
app.geometry("%dx%d"%(wdth,hgt))
app.maxsize(1200,500)
app.minsize(1200,500)
app.title("PRESENT")


tabview = customtkinter.CTkTabview(master=app)
tabview.pack(fill="both",expand=1)

tabview.add("Encriptar")  # add tab at the end
tabview.add("Desencriptar")  # add tab at the end
tabview.set("Encriptar")  # set currently visible tab


cargar_imagen_encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Encriptar"),font=("Helvetica", 25), text="CARGAR IMAGEN",width=230,height=80, command=cargar_imagen_a_encriptar,compound='left')
cargar_imagen_encriptar_btn.place(x=0,y=0)

encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Encriptar"),font=("Helvetica", 25), text="ENCRIPTAR",width=230,height=80, command=encriptar,compound='left')
encriptar_btn.place(x=0,y=100)

limpiar_encriptar_btn = customtkinter.CTkButton(master=tabview.tab("Encriptar"),font=("Helvetica", 25), text="LIMPIAR",width=230,height=80, command=limpiar_imagenes_encriptar,compound='left')
limpiar_encriptar_btn.place(x=0,y=200)

cargar_imagen_desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Desencriptar"),font=("Helvetica", 25), text="CARGAR IMAGEN",width=230,height=80, command=cargar_imagen_a_desencriptar,compound='left')
cargar_imagen_desencriptar_btn.place(x=0,y=0)

desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Desencriptar"),font=("Helvetica", 25), text="DESENCRIPTAR",width=230,height=80, command=desencriptar,compound='left')
desencriptar_btn.place(x=0,y=100)

limpiar_desencriptar_btn = customtkinter.CTkButton(master=tabview.tab("Desencriptar"),font=("Helvetica", 25), text="LIMPIAR",width=230,height=80, command=limpiar_imagenes_desencriptar,compound='left')
limpiar_desencriptar_btn.place(x=0,y=200)



app.mainloop()