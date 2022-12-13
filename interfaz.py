from tkinter import *
from tkinter import ttk

''' PANTALLA PRINCIPAL DE LA APLCIACION'''
class PantallaPrincipal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(True,False) # Redimensionar la ventana
        self.ventana.title('Pantalla Principal') # Titulo de la ventana
        self.ventana.geometry('1000x700') # Tamaño de la ventana
        self.Centrar(self.ventana, 1000, 700) # Centrar la ventana
        self.ventana.config(bg='#102027')
        self.Ventana() # Llamar a la ventana

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight() # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth() # Ancho de la pantalla

        print("Altura de la pantalla: ", altura_pantalla)
        print("Ancho de la pantalla: ", ancho_pantalla)

        x = (ancho_pantalla // 2) - (ancho // 2) # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2) # Posicion de la ventana
        r.geometry(f'+{x}+{y}') # Posicion de la ventana

    def Ventana(self):
        self.frame = Frame(height=1000, width=700) # Se coloca sobre la ventana
        self.frame.config(bg='#37474f')
        self.frame.pack(padx=10, pady=10)
        Label(self.frame, text="Pantalla 1", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=100)

        self.content = StringVar()
        Entry(self.frame, textvariable=self.content,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=150)

        Button(self.frame, text="Soy un boton",command=self.decir_hola, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=275, y=200)
        
        self.frame.mainloop()

    def decir_hola(self):
        print("Hola mundo de python y de lenguajes")
        var = self.content.get()
        print("Nuestro entry contiene: ", var)
        
a = PantallaPrincipal()