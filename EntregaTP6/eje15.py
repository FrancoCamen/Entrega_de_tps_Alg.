from grafo import Grafo
from random import randint
# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.


class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais if isinstance(pais, list) else [pais]
        self.tipo = tipo

    def __str__(self):
        return (f"Nombre: {self.nombre} - Pais: {self.pais} - Tipo: {self.tipo} .")
    
mi_grafo=Grafo(dirigido=False)
diccionario={}


#point a
m_naturales=[
    Maravilla("Cataratas del Iguazú", ["Argentina","Brasil"], "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Monte Everest", "Nepal", "natural"),
    Maravilla("Aurora Boreal", ["Varios países del norte"], "natural"),
    Maravilla("Parque Nacional Yellowstone", "Estados Unidos", "natural"),
    Maravilla("Glaciar Perito Moreno", "Argentina", "natural"),
    Maravilla("Cañón del Colorado", "Estados Unidos", "natural")
]
m_arquitectonicas=[
    Maravilla("Torre Eiffel", "Francia", "arquitectónica"),
    Maravilla("Machu Picchu", "Perú", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Petra", "Jordania", "arquitectónica"),
    Maravilla("La Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Catedral de Santa María del Fiore", "Italia", "arquitectónica"),
    Maravilla("Opera House de Sídney", "Australia", "arquitectónica")
]
for i in range(7):
    mi_grafo.insert_vertice(m_naturales[i], "nombre")
    mi_grafo.insert_vertice(m_arquitectonicas[i], "nombre")

#point b
for i in m_naturales:
    # busca una Maravilla natural
    pos_ori =mi_grafo.search_vertice(i.nombre, "nombre")
    nodo_ori = mi_grafo.get_element_by_index(pos_ori)

    for j in m_naturales:
        # busca otra Maravilla natural
        pos_des = mi_grafo.search_vertice(j.nombre, "nombre")
        nodo_des = mi_grafo.get_element_by_index(pos_des)

        conectadas = mi_grafo.is_adyacent(nodo_ori[0].nombre ,nodo_des[0].nombre, "nombre")

        if nodo_ori != nodo_des and conectadas==False:
            valor= randint(100,5000);
            mi_grafo.insert_arist(nodo_ori[0].nombre,nodo_des[0].nombre,valor, "nombre")

for i in m_arquitectonicas:
    # busca una Maravilla arq
    pos_ori =mi_grafo.search_vertice(i.nombre, "nombre")
    nodo_ori = mi_grafo.get_element_by_index(pos_ori)

    for j in m_arquitectonicas:
        # busca otra Maravilla arq
        pos_des = mi_grafo.search_vertice(j.nombre, "nombre")
        nodo_des = mi_grafo.get_element_by_index(pos_des)

        conectadas = mi_grafo.is_adyacent(nodo_ori[0].nombre ,nodo_des[0].nombre, "nombre")

        if nodo_ori != nodo_des and conectadas==False:
            valor= randint(100,5000);
            mi_grafo.insert_arist(nodo_ori[0].nombre,nodo_des[0].nombre,valor, "nombre")

print()
mi_grafo.barrido()
print()



# point c
# devuelve el grafo de expansion minima
expansion_minima = mi_grafo.kruskal()
for arbol in expansion_minima:
    nodos = arbol.split(";")
    print()
    for nodo in nodos:
        print(nodo)
print()


# point d
pais = []
for i in m_naturales:
    pos_n = mi_grafo.search_vertice(i.nombre, "nombre")
    nodo_n = mi_grafo.get_element_by_index(pos_n)
    pais_n = nodo_n[0].pais
    
    for j in m_arquitectonicas:
        pos_a = mi_grafo.search_vertice(j.nombre, "nombre")
        nodo_a = mi_grafo.get_element_by_index(pos_a)  
        pais_a = nodo_a[0].pais
        
        if pais_n == pais_a and pais_n not in pais:
            pais.append(pais_n)

print(f"Paises que tiene maravillas naturales y arquitectonicas: {pais}")

# point e
print()  
paises = []
for i in m_naturales:
    pos_a = mi_grafo.search_vertice(i.nombre, "nombre")
    nodo_a = mi_grafo.get_element_by_index(pos_a)
    pais_a = nodo_a[0].pais

    for pais in pais_a:
        if len(paises) != 0:
            encontro = False
            for posicion in paises:
                if posicion[0] == pais:
                    posicion[1] += 1
                    encontro = True
            if encontro == False:
                paises.append([pais, 1])      
        else:
            paises.append([pais, 1])
for pais in paises:
    if pais[1] != 1:
        print(f"El pais {pais[0]} tiene {pais[1]} maravillas naturales")

print()  
paises = []
for i in m_arquitectonicas:
    pos_a = mi_grafo.search_vertice(i.nombre, "nombre")
    nodo_a = mi_grafo.get_element_by_index(pos_a)
    pais_a = nodo_a[0].pais

    for pais in pais_a:
        if len(paises) != 0:
            encontro = False
            for posicion in paises:
                if posicion[0] == pais:
                    posicion[1] += 1
                    encontro = True
            if encontro == False:
                paises.append([pais, 1])      
        else:
            paises.append([pais, 1])
for pais in paises:
    if pais[1] != 1:
        print(f"El pais {pais[0]} tiene {pais[1]} maravillas arquitectonicas")



