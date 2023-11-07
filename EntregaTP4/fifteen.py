from lista_lista import Lista
from random import randint

class Entrenador():

    def __init__(self, nombre, ct_ganados, cb_perdidas, cb_ganadas):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas
    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg:{self.cb_ganadas}-cbp:{self.cb_perdidas}'

class Pokemon():
    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Entrenador1', randint(1, 10), 2, 8)
e2 = Entrenador('Entrenador2', randint(1, 10), 2, 7)
e3 = Entrenador('Entrenador3', randint(1, 10), 38 , 7)

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20), 'volador')
p4 = Pokemon('flareon', 'fuego', randint(1, 20), 'planta')
p5 = Pokemon('leafeon', 'planta', randint(1, 20))
p6 = Pokemon('pikachu', 'electrico', randint(1, 20))
p7 = Pokemon('tyrantrum', 'electrico', randint(1, 20))
p8 = Pokemon('terrakion', 'electrico', randint(1, 20))
p9 = Pokemon('wingull', 'electrico', randint(1, 20))

pokemons = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


def cantidadPokemons(lista_entrenadores, nombre_entrenador):
    index = lista_entrenadores.search(nombre_entrenador, 'nombre')    
    if index!= None:
        value = lista_entrenadores.get_element_by_index(index)
        entrenador, pokemons = value[0], value[1]
        print(f"{entrenador.nombre} tiene {pokemons.size()} pokemons")

def gano_mas_tres(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()-1):
        value = lista_entrenadores.get_element_by_index(i)
        if value[0].ct_ganados > 3:
            print(value[0]) 


def mayorTorneosNivel(lista_entrenadores):
    mayor_cantidad = 0
    pos_mayor = 0

    for pos in range(1, lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]
        if entrenador.ct_ganados > mayor_cantidad:
            pos_mayor = pos
            mayor_cantidad = entrenador.ct_ganados

    valor = lista_entrenadores.get_element_by_index(pos_mayor)
    entrenador, sublista = valor[0], valor[1]

    if sublista.size() > 0:
        pokemon_level = 0
        for pos in range(1, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nivel > pokemon_level.nivel:
                pokemon_level = pokemon
    print(f'El pokemon de mayor nivel del entrenador con mas torneos gandos es {pokemon_level.nombre} {pokemon_level.nivel} ')
    

def unEntrenador(lista_entrenadores, entrenador):
    index = lista_entrenadores.search(a, 'nombre')    
    if index != None:
        value = lista_entrenadores.get_element_by_index(index)
        entrenador, sublista = value[0], value[1]
        print(f"Se muestran los pokemons del entrenador {entrenado.nombre}")
        sublista.barrido()    


def porcentaje79(lista_entrenadores):  
    for i in range(0, lista_entrenadores.size()):
            value = lista_entrenadores.get_element_by_index(i)
            total_batallas = value[0].cb_ganadas + value[0].cb_perdidas
            porcentaje = total_batallas * 0.79
            if value[0].cb_ganadas > porcentaje:
                print(value[0])

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promediar(lista_entrenadores, entrenador): 
    promedio = 0 
    cont = 0
    index = lista_entrenadores.search(entrenador, 'nombre')    
    if index != None:
        value = lista_entrenadores.get_element_by_index(index)
        for i in range(0, value[1].size()):
            valor = value[1].get_element_by_index(i)
            promedio = promedio + valor.nivel
            cont += 1     
        if cont > 0:
            final = promedio / cont  
            print(final)    

def determinadoPokemon(lista_entrenadores, pokemon):
    for i in range(0, lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(i)
        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            if valor.nombre in pokemon:
                print(value[0].nombre)

# i. mostrar los entrenadores que tienen Pokémons repetidos;
def pokemonsRepetidos(lista_entrenadores):
    entrenadores_por_pokemon = {}

    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        for pokemon in range(entrenador[1].size()):
            nombre_pokemon = entrenador[1].get_element_by_index(pokemon).nombre
            if nombre_pokemon in entrenadores_por_pokemon:
                entrenadores_por_pokemon[nombre_pokemon].append(entrenador[0].nombre)
            else:
                entrenadores_por_pokemon[nombre_pokemon] = [entrenador[0].nombre]
                
    for nombre_pokemon, entrenador_list in entrenadores_por_pokemon.items():
        if len(entrenador_list) > 1:
            if len(entrenador_list) != len(set(entrenador_list)):
                print(f'{entrenador_list[0]} tiene mas de un {nombre_pokemon}')
            
# f. (Mostrar supongo) los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
def mostrar_tipo(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        
        valor = lista_entrenadores.get_element_by_index(i)
        for j in range(0, valor[1].size()):
            value = valor[1].get_element_by_index(j)
            if (value.tipo in 'agua' and value.subtipo in 'volador') or (value.tipo == 'fuego' and value.subtipo == 'planta')  :
                print(f'{valor[0].nombre} tiene su pokemon {value.nombre} tipo: {value.tipo} y subtipo: {value.subtipo}') 

#  j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
def determinarPokemons(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        
        value = lista_entrenadores.get_element_by_index(i)
        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            if valor.nombre in 'tyrantrum':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'terrakion':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'wingull':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            else:
                None
                

def ingresoDatos(lista_entrenadores, entrenador, pokemon):
    index = lista_entrenadores.search(entrenador, 'nombre')    
    if index != None:
        value = lista_entrenadores.get_element_by_index(index)
        entrenador, sublista = value[0], value[1]
        cont = 0
        for j in range(0, sublista.size()):
            valor = sublista.get_element_by_index(j)
            if valor.nombre in npokemon:
                cont += 1
                print(f'estos son los datos del entrenador: {entrenador}')
                print(f'estos son los datos del pokemon: {valor}')
                

entrenador = input('Ingrese un entrenador para conocer sus pokemones:  ')
cantidadPokemons(lista_entrenadores, entrenador)

print('Listar los entrenadores que hayan ganado más de tres torneos')
gano_mas_tres(lista_entrenadores)

print('Ell Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados')
mayorTorneosNivel(lista_entrenadores)

entrenador = input('d. mostrar todos los datos de un entrenador y sus Pokémos: ')
unEntrenador(lista_entrenadores, entrenador)

print('Mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %')
porcentaje79(lista_entrenadores)

entrenador = input('g. el promedio de nivel de los Pokémons de un determinado entrenador: ')
promediar(lista_entrenadores, entrenador)

print('Determinar cuántos entrenadores tienen a un determinado Pokémon')
pokemon_input = input('Deseas ver q entrenadores tienen el pokemon:  ')
determinadoPokemon(lista_entrenadores, pokemon_input)

print('ostrar los entrenadores que tienen Pokémons repetidos')
pokemonsRepetidos(lista_entrenadores)

print('Entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador')
mostrar_tipo(lista_entrenadores)

print('Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull')
determinarPokemons(lista_entrenadores)

print('Determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados;')
nombreentrenador = input('Que entrenedor desea buscar?')
nombrepokemon = input('Que pokemon decea buscar?')
ingresoDatos(lista_entrenadores, nombreentrenador, nombrepokemon)

