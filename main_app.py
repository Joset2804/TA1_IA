from importlib.resources import path
import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox
from data_in import read
from data_in import text_to_list
import numpy as np
from hillClimbing import hillClimbing
from graficos import show_results

class MainApp:
    def styles(app, win):
        container_size = 3
        #LABELS
        app.label1=Label(win, text="Altura de contenedores: ")
        app.label2=Label(win, text="Lista de alturas de cajas: ")
        app.label3=Label(win, text='Optimización de Bin Packing de una dimensión',font=("Arial Bold",18))
        app.label1.place(x=50, y=70)
        app.label2.place(x=45, y=120)
        app.label3.place(x=25, y=20)

        #TEXTSCROLL
        app.txt=scrolledtext.ScrolledText(window, width=40, height=10)
        app.txt.grid(column=0, row=0)
        app.txt.place(x=500, y=150)

        #RADIO BUTTON
        app.v0 = IntVar()
        app.v0.set(0)
        app.radio1 = Radiobutton(win,text="Descendente", variable=app.v0, value= 0)
        app.radio2 = Radiobutton(win,text="Ascendente", variable=app.v0, value= 1)
        app.radio3 = Radiobutton(win,text="Desordenado", variable=app.v0, value= 2)
        app.radio1.place(x=50,y=160)
        app.radio2.place(x=170,y=160)
        app.radio3.place(x=290,y=160)

        #INPUTS
        app.text1=Entry()
        app.text1.insert(END,str(container_size))
        app.text2=Entry()
        app.text2.insert(END,"3,2,2,1,1")
        app.text1.place(x=200, y=70)
        app.text2.place(x=200, y=120)

        #BUTTONS
        app.btn1=Button(win, text='Ingresar Archivo .txt', command=app.read_txt)
        app.btn2=Button(win, text='Optimizar',command=app.start)
        app.btn1.place(x=150, y=200)
        app.btn2.place(x=250, y=200)

    def read(app):
        path = fd.askopenfilename()
        container_size, boxes = read(path)
        app.text1.delete(0,END)
        app.text2.delete(0,END)
        var_boxes = str(boxes)
        var_boxes = var_boxes[1:-1]
        #Ambos valores son 0 cuando una caja excede la altura del contenedor
        if (container_size == 0) and (boxes == 0):
            messagebox.showerror("ERROR DE LECTURA", "La altura de las cajas deben ser menores a la altura del contenedor")
        else:
            app.text1.insert(END,str(container_size))
            app.text2.insert(END,var_boxes)

    def begin(app):
         #obtención de datos
        container_size = int(app.text1.get())
        boxes = text_to_list(app.text2.get())
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
            if app.v0.get() == 0:
                boxes.sort(reverse=True)
            elif app.v0.get() == 1:
                boxes.sort()
            var_boxes = str(boxes)
            var_boxes = var_boxes[1:-1]
            app.txt.insert(END,"RESULTADOS\n----------------------------------------\nLas alturas de las cajas a colocar son  las siguientes: " + str(var_boxes) + "\n")
            #SE EJECUTA EL ALGORITMO DE OPTIMIZACIÓN
            start = time.time()
            containers = hillClimbing(container_size,boxes)
            end = time.time()
            print("Algorithm Time Execution:",(end-start)*1000)
            app.txt.insert(END,"La solución óptima local encontrada es  distribuir las cajas en " + str(len(containers))+" contenedores\n")
            np_containers = np.array(containers)
            app.txt.insert(END,"Agrupados de la siguiente manera:\n")
            for container,i in zip(np_containers,range(len(np_containers))):
                app.txt.insert(END,"Contenedor "+str(i+1)+": "+str(container)+"\n")
            app.txt.insert(END,"\n")
            #MUESTRA LOS RESULTADOS GRAFICAMENTE
            show_results(container_size,containers)


window=Tk()
mywin=MainApp(window)
window.title('BIN PACKING DE UNA DIMENSION')
window.geometry("800x250+10+10")
window.mainloop()