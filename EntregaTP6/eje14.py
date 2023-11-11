from grafo import Grafo
from random import randint

house = Grafo(dirigido = False)
habitaciones = ["cocina","comedor","cochera", "quincho", "baño1","baño2","habitacion1","habitacion2","sala de estar", "terraza","patio"]

for i in habitaciones:
    house.insert_vertice(i)

#primero se le carga a cada habitacion las aristas hasta que tenga 3 coneciones
for i in habitaciones:
    pos_ori = house.search_vertice(i)
    nodo_ori = house.get_element_by_index(pos_ori)
    
    if nodo_ori[1].size() < 3:
        k=0   #k es el contador de habitaciones
        condicion = True   #es False si k>= len(habitaciones) o nodo[1].size() >3

        while condicion:
            if k >= len(habitaciones):
                condicion = False
                break
            else:
                #busca un nodo de destino
                hab = habitaciones[k]
                pos_des = house.search_vertice(hab)
                nodo_des = house.get_element_by_index(pos_des)

                #se verifican que no sean adyacentes
                conectados = house.is_adyacent(nodo_ori[0], nodo_des[0])

                if nodo_des[1].size() < 3 and nodo_ori[0]!=nodo_des[0] and conectados == False:
                    peso = randint(1, 11)
                    house.insert_arist(nodo_ori[0], nodo_des[0], peso)
                    if nodo_ori[1].size() == 3:
                        condicion = False
                        break
                k +=1

house.insert_arist("patio", "quincho", randint(1, 11))
house.insert_arist("sala de estar", "quincho", randint(1, 11))
house.insert_arist("terraza", "comedor", randint(1, 11))
house.insert_arist("baño2", "comedor", randint(1, 11))


#devuelve el grafo de expansion minima
expansion_minima = house.kruskal()
for arbol in expansion_minima:
    nodos = arbol.split(";")
    metros_cables = 0
    for nodo in nodos:
        metros_cables += int(nodo.split("-")[2])
print()
print(f"La cantidad me metros de cables es {metros_cables}")
print()


camino = house.dijkstra("habitacion1","sala de estar")
cables = 0
for i in range(camino.size()):
    if camino.on_top()[0] == "sala de estar":
        cables = camino.on_top()[1]
    print(camino.pop())
print()
print(f"La cantidad de cables para conectar la habitacion 1 con la sala de estar es {cables}")
print()





