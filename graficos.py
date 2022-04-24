from turtle import color
import numpy as np
import matplotlib.pyplot as plt

#Para el caso donde exista solo un contenedor
def single_draw(container_size,containers,aux):
    for container, n in zip(containers,range(len(containers))):
        btm = 0
        container_label = "Contenedor " + str(n+1)
        for i in range(len(container)):
            if i == len(container) - 1:
                aux.bar(container_label, container[i],  yerr=[[0],[container_size-btm-container[i]]], edgecolor="black",linewidth=1, bottom=btm)
            elif i == 0:
                aux.bar(container_label, container[i],  edgecolor="black",linewidth=1)
            else:
                aux.bar(container_label, container[i],  edgecolor="black",linewidth=1, bottom=btm)
            btm += container[i]

#Para el caso donde exista mas de un contenedor
def multi_draw(container_size,containers,aux):
    for container, graph, n in zip(containers,aux,range(len(containers))):
        btm = 0
        container_label = "Contenedor " + str(n+1)
        for i in range(len(container)):
            if i == len(container) - 1:
                graph.bar(container_label, container[i],  yerr=[[0],[container_size-btm-container[i]]], edgecolor="black",linewidth=1, bottom=btm, color="#1976D2")
            elif i == 0:
                graph.bar(container_label, container[i],  edgecolor="black",linewidth=1, color="#FFEB3B")
            ##else:
                #graph.bar(container_label, container[i],  edgecolor="black",linewidth=1, bottom=btm, color="#8BC34A")
            btm += container[i]

#Para dibujar todos los contenedores calculados
def show_results(container_size,containers):
    fig, aux = plt.subplots(1,len(containers),figsize=(10+len(containers),7),sharey=True)
    if len(containers) == 1:
        single_draw(container_size,containers,aux)
        aux.set_ylabel('Espacio ocupado', fontsize = 20)
    else:
        multi_draw(container_size,containers,aux)
        aux[0].set_ylabel('Espacio ocupado', fontsize = 20)
    fig.suptitle('Grupo de contenedores', fontsize = 20)
    plt.show()