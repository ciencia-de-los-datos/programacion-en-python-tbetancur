"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

data= open('data.csv' , newline='')  
data = csv.reader(data, delimiter='\t')



def pregunta_01():
    """
    Retorne la suma de la segunda columna

    Rta/
    214

    """
    colum2 = 0
    for row in data:
        colum2 += int(row[1])

    return colum2





def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    counter = {}
    for row in data:
        
        if row[0] in counter.keys():
            counter[row[0]] += 1
        else:
            counter[row[0]] = 1
            
    return sorted(counter.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    counter = {}
    for row in data:
        if row[0] in counter.keys():
            counter[row[0]] += int(row[1])
        else:
            counter[row[0]]= int(row[1])
                      
    return sorted(counter.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    counter = {}
    for row in data:
        month = row[2].split('-')[1]
        if month in counter.keys():
            counter[month] += 1
        else:
            counter[month] = 1
            
    return sorted(counter.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    max_min = {}
    for row in data:
        letter = row[0]
        value = int(row[1])
         
        if letter not in max_min:
            max_min[letter] = [value,value]
        else:
            max_min[letter][0]= max(max_min[letter][0], value)
            max_min[letter][1]= min(max_min[letter][1], value)
        r_max_min = [(letter, max_min[letter][0],max_min[letter][1]) for letter in sorted(max_min)]
    return r_max_min  



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores = {}
    valores_min = {}
    valores_max = {}

    for row in data:
        diccionario = dict(item.split(':') for item in row[4].split(','))
        for clave, valor in diccionario.items():
            valor = int(valor)
            if clave in valores:
                valores[clave].append(valor)
            else:
                valores[clave] = [valor]

    for clave, lista_valores in valores.items():
        valores_min[clave] = min(lista_valores)
        valores_max[clave] = max(lista_valores)

    lista_tuplas = [(clave,valores_min[clave], valores_max[clave]) for clave in valores.keys()]
    return sorted(lista_tuplas)

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    counter = {}
    for row in data:
        value = int(row[1])
        if value in counter.keys():
            counter[value].append(row[0])
        else:
            counter[value]= [row[0]]
                   
    return sorted (counter.items())   


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    counter = {}
    for row in data:
        value = int(row[1])
        if value in counter.keys():
            counter[value].append(row[0])
        else:
            counter[value]= [row[0]]
                   
    return [(r[0], sorted(list(set(r[1])))) for r in sorted(counter.items())]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    counter = {}
    for row in data:
        pairs = row [4].split(',')
        for pair in pairs:
            value = pair.split(':')
            value[1] = int (value[1])
            if value [0] in counter.keys():
                counter[value[0]] += 1
            else:
                counter[value[0]]=1
    return counter


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    counter = []
    for row in data:
        counter.append((
            row[0],
            len (row[3].split(',')),
            len(row[4].split(','))
            ))
    return counter


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    for fila in data:
        numero = fila[1]
        elementos = fila[3].split(',')
        for elemento in elementos:
            letra = elemento.split(',')[0]
            if letra in suma_por_letra:
                suma_por_letra[letra] += float(numero)
            else:
                suma_por_letra[letra] = float(numero)

            
    return dict(sorted(suma_por_letra.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    counter ={}
    for row in data:
        if row[0] not in counter.keys():
            counter[row[0]] = 0
        pairs = row[4].replace (':',',').split(',')
        for pair in pairs:
            if pair.isdigit():
                counter[row[0]] += int (pair)
    return counter
