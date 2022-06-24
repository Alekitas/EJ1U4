from ast import Raise
from cgitb import text
from ntpath import altsep
from tkinter import *
from tkinter import ttk, messagebox
class aplicacion():
    __ventana=None
    __peso=None
    __altura=None
    __imc=None
    __composicion=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.geometry('290x290')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(0,0)
        
        mainframe=ttk.Frame(self.__ventana,padding="3 3 12 12")
        mainframe.grid(column=0, row=1,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'groove'

        self.__altura= StringVar()
        self.__peso = StringVar()
        self.__imc=StringVar()
        self.__composicion=StringVar()

        ttk.Label(mainframe,text="Altura: ").grid(column=0,row=0)
        self.alturaEntry=ttk.Entry(mainframe,width=40,textvariable=self.__altura)
        self.alturaEntry.grid(column=0,row=1)
        ttk.Label(mainframe,text="cm").grid(column=2,row=1)
        
        ttk.Label(mainframe,text="Peso:").grid(column=0,row=2)
        self.pesoEntry=ttk.Entry(mainframe,width=40,textvariable=self.__peso)
        self.pesoEntry.grid(column=0,row=3)
        ttk.Label(mainframe,text="kg").grid(column=2,row=3)
        
        ttk.Label(mainframe,text="IMC: ").grid(column=0,row=4,sticky=(W))
        ttk.Label(mainframe,textvariable=self.__imc).grid(column=0,row=4)
        ttk.Label(mainframe,text="Composicion: ").grid(column=0,row=5,sticky=(W))
        ttk.Label(mainframe,textvariable=self.__composicion).grid(column=0,row=5,sticky=(S))
        ttk.Button(self.__ventana,text="Limpiar",command=self.Limpiar).grid(column=0,row=4,sticky=(W))
        ttk.Button(self.__ventana,text="Calcular",command=self.Calcular).grid(column=0,row=4,sticky=(E))
        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def Calcular(self):
        try:
            alt=float(self.alturaEntry.get())/100
            pes=float(self.pesoEntry.get())
            imc=pes/alt**2
            self.__imc.set(imc)
            if imc < 18.5:
                self.__composicion.set('Peso inferior al normal')
            elif imc >= 18.5 and imc <=24.9:
                self.__composicion.set('Normal')
            elif imc >= 25 and imc <= 29.9:
                self.__composicion.set('Peso superior al normal')
            elif imc > 30:
                self.__composicion.set('Obesidad')
        except ValueError:
            messagebox.showerror(title='Error de tipo, ingrese un valor numerico')
            self.__altura.set=('')
            self.__pes.set=('')
            self.__alturaEntry.focus()
    def Limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.__imc.set('')
        self.__composicion.set('')