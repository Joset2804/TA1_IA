import numpy as np

# Lee el archivo y lo convierte en una lista
def text_to_list(string):
    string = string.split(",")
    data_set = []
    for data in string:
        data_set.append(int(data))
    return data_set

def read(path):

    # Lee el archivo
    """ 
    Funcion que permite leer un archivo de texto para obtener los valores
    correspondientes devolviendo la capacidad de los contenedores y 
    el número de cajas ordenadas de mayor a menor.
    """

    #Obtenemos los archivos
    file = open(path,"r")
    f1=file.readlines()

    #Se filtra el archivo para obtener la capacidad de los contenedores
    data = []
    boxes = []
    for line in f1:
        data.append([str(n) for n in line.split(' ')])

    #Obtenemos los datos de los contenedores
    container_size = int(data[0][0])
    for i in range(1,len(data)):
        n_box = int(data[i][0])
        for time in range(n_box):
            valor = int(data[i][1])
            if valor > container_size: return 0,0
            boxes.append(valor)
    return container_size, boxes
