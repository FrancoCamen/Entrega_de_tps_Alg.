# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:



from Lista import Lista

Lista = Lista()


class heroes():
    def __init__(self, nombre, año, casa, biografia):
        self.nombre = nombre
        self.año = año
        self.casa = casa
        self.biografia = biografia
    def __str__(self):
            return f'{self.nombre} - {self.año} - {self.casa} - {self.biografia}'
def superhéroes(lista):
    lista.insert(heroes('Wolverine', 1974, 'Marvel',
                 'Mutante con garras retráctiles y poder de regeneración, luchador incansable y miembro de los X-Men.'), "nombre")
    lista.insert(heroes('Linterna Verde', 1940, 'DC',
                 'Héroe con anillo que crea manifestaciones de energía y defiende el universo contra amenazas intergalácticas.'), "nombre")
    lista.insert(heroes('Dr. Strange', 2014, 'Marvel',
                 'Brillante cirujano convertido en hechicero maestro, protector del multiverso y manipulador del tiempo y la realidad.'), "nombre")
    lista.insert(heroes('Capitana Marvel', 2019, 'Marvel',
                 'Piloto de combate transformada en una poderosa heroína cósmica con fuerza, velocidad y energía cósmica ilimitada.'), "nombre")
    lista.insert(heroes('Mujer Maravilla', 1941, 'DC',
                 'Princesa amazona con habilidades sobrehumanas, sabia y valiente defensora de la justicia y la paz.'), "nombre")
    lista.insert(heroes('Flash', 1939, 'DC',
                 ' Velocista extraordinario con la capacidad de correr a velocidades superlumínicas y alterar el tiempo. usa armadura'), "nombre")
    lista.insert(heroes('Star-Lord', 1976, 'Marvel',
                 'Carismático piloto espacial, líder de los Guardianes de la Galaxia, experto en combate y aficionado a la música.'), "nombre")

    lista.insert(heroes('Iron Man', 1963, 'Marvel',
                 'Genio multimillonario, inventor y filántropo, protegido por una traje tecnológica de alta potencia y defensor incansable de la justicia.'), "nombre")





#ordeno la lista


def flashlight_green(lista):
    lista.order_by(criterio="nombre")
    #busco a linterna verde
    index = lista.search_r("Linterna Verde", 0, lista.size(), "nombre") 
    # print(index)
    if index != None:
        lista.delete("Linterna Verde", criterio = "nombre")
    lista.barrido()
    # b. mostrar el año de aparición de Wolverine;
#busco a wolverine
def year_wolverine(lista):
    indice = lista.search_r("Wolverine", 0, lista.size()-1, "nombre")
    if indice != None:
        year_wol = lista.get_element_by_index(indice)
        print(year_wol.año)
# c. cambiar la casa de Dr. Strange a Marvel;    
def change_house(lista):
    indice = lista.search_r("Dr. Strange", 0, lista.size()-1, "nombre")
    if indice != None:
        new_house = lista.get_element_by_index(indice)
        new_house.casa = 'DC'
    lista.barrido()
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# falta hacer cuando el texto dice armadura y traje

def say_traje_armadura(lista):
    
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if 'armadura' in heroe.biografia:
            print(f'en la biografia de {heroe.nombre} se encontro la palabra armadura')
        elif 'traje' in heroe.biografia:
            print(f'en la biografia de {heroe.nombre} se encontro la palabra traje')
                
        else:
            print('no se encontro ninguna palabra pedida')

# h. listar los superhéroes que comienzan con la letra B, M y S;
def first_b_m_s(lista):
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if heroe.nombre[0] == 'B':
            print(f'La primer letra de {heroe.nombre} es B')
        if heroe.nombre[0] == 'M':
            print(f'La primer letra de {heroe.nombre} es M')
        if heroe.nombre[0] == 'S':
            print(f'La primer letra de {heroe.nombre} es S')
        else:
            print('no se encontraron coincidencias')  
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
def antes_de_un_año(lista):
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        if heroe.año < 1963:
            print(f'El personaje {heroe.nombre} de la casa cinematografica {heroe.casa} aparecio antes de 1963')
        elif heroe.año == 1963:
            print(f'El personaje {heroe.nombre} aparecio en el año 1963')
                
        else:
            print(f'El personaje {heroe.nombre} aparecio luego de 1963')
                
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
def house_woman_amazing_capitana_marvel(lista):
    indice = lista.search_r("Capitana Marvel", 0, lista.size()-1, "nombre")
    if indice != None:
            new_house = lista.get_element_by_index(indice)
            print(f'Capitana Marvel es de {new_house.casa}')

    
# g. mostrar toda la información de Flash y Star-Lord;
def info_flash_star(lista):
    indice = lista.search_r("Flash", 0, lista.size()-1, "nombre")
    if indice != None:
        new_house = lista.get_element_by_index(indice)
        print(f'Biografia de Flash: {new_house.biografia}')

    indice2 = lista.search_r("Star-Lord", 0, lista.size()-1, "nombre")
    if indice2 != None:
        house = lista.get_element_by_index(indice2)
        print(f'Biografia de Star-Lord: {house.biografia}')

# i. determinar cuántos superhéroes hay de cada casa de comic.
def dc_marvel(lista):
    cont = 0
    for i in range(lista.size()):
        heroe = lista.get_element_by_index(i)
        
        if heroe.casa == 'DC':
            cont += 1
        else:
            cont += 0
    return cont



superhéroes(Lista)
print('Elinacion de Linterna verde')
flashlight_green(Lista)
print()
print('--------------------------------------------------------------------')
print('Fecha de aparicion de wolverine')
year_wolverine(Lista)
print()
print('--------------------------------------------------------------------')
print('Actualizacion de Dr. Strange a casa DC')
print()
change_house(Lista)
print()
print('--------------------------------------------------------------------')
print()
say_traje_armadura(Lista)
print()
print('--------------------------------------------------------------------')
print()
first_b_m_s(Lista)
print()
print('--------------------------------------------------------------------')
print()
antes_de_un_año(Lista)
print()
print('--------------------------------------------------------------------')
print()
house_woman_amazing_capitana_marvel(Lista)
print()
print('--------------------------------------------------------------------')
print()
info_flash_star(Lista)
print()
print('--------------------------------------------------------------------')
print()
cont = dc_marvel(Lista)
print(f'DC tiene {cont} personajes en la lista')
print(f'Marvel tiene {Lista.size() - cont} personajes')
