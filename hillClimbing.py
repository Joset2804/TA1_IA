#Heurística
def heuristic(container,newBox,containerSize):
    h = 0
    for box in container:
        h += box
    h += newBox
    if h > containerSize:  
        return 0   
    else: 
        return h                         

#Función para encontrar la caja que mejor se adapta
def findBestBox(container,boxes,containerSize):
    heuristics = [] 
    for box in boxes:
        heuristics.append(heuristic(container,box,containerSize))
    if heuristics:
        max_h = max(heuristics)
        if max_h != 0: 
            selection = heuristics.index(max_h) 
            container.append(boxes.pop(selection))
            return True 
    return False

#Función Hill Climbing
def hillClimbing(containerSize,boxes):
    containers = [[boxes.pop(0)]]
    print("Cajas empacadas",containers)
    index = 0
    while boxes:
        if not findBestBox(containers[index],boxes,containerSize):
            containers.append([boxes.pop(0)])
            index += 1
        print("Cajas empacadas",containers)
    print("Resuelto")
    return containers