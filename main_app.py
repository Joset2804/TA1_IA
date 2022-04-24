from cProfile import label
from importlib.resources import path
import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox
from turtle import color

from pyparsing import White
from data_in import read
from data_in import text_to_list
import numpy as np
from hillClimbing import hillClimbing
from graficos import show_results

class MyWindow:
    def __init__(self, win):
        container_size = 3
        
        #LABELS
        self.label1=Label(win, text="Altura de contenedores: ")
        self.label2=Label(win, text="Lista de alturas de cajas: ")
        self.label3=Label(win, text='Bin Packing Optimization with Hill Climbing',font=("Arial Bold",18))
        self.label1.place(x=50, y=70)
        self.label2.place(x=50, y=120)
        self.label3.place(x=25, y=20)
        self.label1['bg'] = '#CDDC39'
        self.label2['bg'] = '#CDDC39'
        self.label3['bg'] = '#CDDC39'

        #TEXTSCROLL
        self.txt=scrolledtext.ScrolledText(window, width=60, height=10)
        self.txt.grid(column=0, row=0)
        self.txt.place(x=25, y=250)

        #RADIO BUTTON
        self.v0 = IntVar()
        self.v0.set(0)
        self.radio1 = Radiobutton(win,text="Descendente", variable=self.v0, value= 0)
        self.radio2 = Radiobutton(win,text="Ascendente", variable=self.v0, value= 1)
        self.radio3 = Radiobutton(win,text="Desordenado", variable=self.v0, value= 2)
        self.radio1.place(x=380,y=70)
        self.radio2.place(x=380,y=120)
        self.radio3.place(x=380,y=170)
        self.radio1['bg'] = '#CDDC39'
        self.radio2['bg'] = '#CDDC39'
        self.radio3['bg'] = '#CDDC39'

        #INPUTS
        self.text1=Entry()
        self.text1.insert(END,str(container_size))
        self.text2=Entry()
        self.text2.insert(END,"3,2,2,1,1")
        self.text1.place(x=200, y=70)
        self.text2.place(x=200, y=120)

        #BUTTONS
        self.btn1=Button(win, text='Ingresar Archivo .txt', command=self.read, font=("Arial Bold",10))
        self.btn2=Button(win, text='Optimizar',command=self.begin, font=("Arial Bold",10))
        self.btn1.place(x=100, y=200)
        self.btn2.place(x=250, y=200)
        self.btn1['bg'] = '#1976D2'
        self.btn1.configure(fg="white")
        self.btn2['bg'] = '#1976D2'
        self.btn2.configure(fg="white")


    def read(self):
        path = fd.askopenfilename()
        container_size, boxes = read(path)
        self.text1.delete(0,END)
        self.text2.delete(0,END)
        var_boxes = str(boxes)
        var_boxes = var_boxes[1:-1]
        #Ambos valores son 0 cuando una caja excede la altura del contenedor
        if (container_size == 0) and (boxes == 0):
            messagebox.showerror("ERROR DE LECTURA", "La altura de las cajas deben ser menores a la altura del contenedor")
        else:
            self.text1.insert(END,str(container_size))
            self.text2.insert(END,var_boxes)

    def begin(self):
         #obtención de datos
        container_size = int(self.text1.get())
        boxes = text_to_list(self.text2.get())
        check = True
        #Verificar que las cajas no excedan a la altura del contenedor
        for box in boxes:
            if box > container_size: check = False
        #Verifica que el contenedor tenga un espacio y no sea nulo
        if container_size < 1: check = False
        if not check:
            messagebox.showerror("ERROR DE LECTURA", "La altura de las cajas deben ser menores a la altura del contenedor")
        else:
            #SE CONFIGURA EL ESTADO INICIAL
            if self.v0.get() == 0:
                boxes.sort(reverse=True)
            elif self.v0.get() == 1:
                boxes.sort()
            var_boxes = str(boxes)
            var_boxes = var_boxes[1:-1]
            self.txt.insert(END,"RESULTADOS\n----------------------------------------\nLas alturas de las cajas a colocar son  las siguientes: " + str(var_boxes) + "\n")
            #SE EJECUTA EL ALGORITMO DE OPTIMIZACIÓN
            start = time.time()
            containers = hillClimbing(container_size,boxes)
            end = time.time()
            print("Algorithm Time Execution:",(end-start)*1000)
            self.txt.insert(END,"La solución óptima local encontrada es  distribuir las cajas en " + str(len(containers))+" contenedores\n")
            np_containers = np.array(containers)
            self.txt.insert(END,"Agrupados de la siguiente manera:\n")
            for container,i in zip(np_containers,range(len(np_containers))):
                self.txt.insert(END,"Contenedor "+str(i+1)+": "+str(container)+"\n")
            self.txt.insert(END,"\n")
            #MUESTRA LOS RESULTADOS GRAFICAMENTE
            show_results(container_size,containers)


window=Tk()
mywin=MyWindow(window)
window.title('BIN PACKING WITH HILL CLIMBING')
window.geometry("550x450+10+10")
window['bg'] = '#CDDC39'
window.mainloop()