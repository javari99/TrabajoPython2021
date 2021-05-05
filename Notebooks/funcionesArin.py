#Funciones de Arin
import itertools
import numpy as np
from babel.numbers import parse_decimal
import regex as re
from regex.regex import match


def twoSum(arr : list, target : float) -> list:
    """[summary]
    Busca todos los pares de números de la lista que suman al target\n
    Args:
        arr (list): Lista de números\n
        target (float): Numero deseado de suma\n

    Returns:
        [list] : Lista con todos los candidatos que cumplen con la suma\n
    """
    matches = set()
    for x in arr:
        for y in arr:
            if round(x + y, 2) == target:
                if not((y,x) in matches):
                    matches.add((x,y))
    return list(matches)


def twoSumGetMostLikely(arr : list, target : float) -> tuple:
    """[summary]
    Busca todos los pares de números de la lista que suman target y filtra aquellos 
    que no vayan a ser el precio final\n
    Args:
        arr (list): Lista de numeros por los que se buscan el target\n
        target (float): El número deseado que encontrar con la suma\n

    Returns:
        [tuple] : Los dos candidatos para el precio\n
    """
    candidates = twoSum(arr,target)
    # Buscamos el máximo de todos, que probablemente sea la base imponible
    max = -1
    for i in candidates:
        for el in i:
            max = el if el > max else max

    # Devolvemos el que tenga el maximo
    for i in candidates:
        if max in i:
            return i


def findNIF(instring):
    """[summary]
    Funcion que busca un NIF dentro de un string\n
    Args:
        instring (string) : String en el que buscar el NIF\n
    Returns:
        [list]: Lista con todos los NIF del fichero\n
    """
    matches = re.findall('([A-Z]-?\d{8}|\d{8}[-| ]?[A-Z]|[A-Z]-?\d{10}|\d{10}[-| ]?[A-Z])\s', \
                instring)
    return matches


def getAllPricesAndTotal(data : str) -> tuple:
    """[summary]
        Busca todos los precios peresentes en el fichero
    Args:
        data (str): [description]

    Returns:
        tuple: [description]

    Internal workings:
    Tenemos dos regex, para numero americanos y para numeros en español. usamos babel para hacer
    el parse de esos numeros.
    Una vez tenemos los numeros filtramos en dos listas arr y removers, arr es una lista con todos los precios
    positivos del fichero y removers es una lista con todos los precios negativos(se añade para solucionar el problema
    de devolución en IVALINEAS2 (1).txt).
    Con los removers lo que hacemos es borrar los precios que sean de devoluciones
    Finalmente supondremos que el precio total de la factura es el valor más alto de la lista de precios.
    """
    #Recogemos el precio total de la factura
    matches = re.findall('-?(?:\d+?\.?)(?:\d*\,\d{2})0?(?:\s|€)', data)
    matches = [element.replace("€", "") for element in matches] #Eliminamos el símbolo de €
    #convertimos a numeros y luego filtramos el maximo
    matches = [float(parse_decimal(d, locale="es_ES")) for d in matches]
    arr = []
    removers = []
    if matches:
        # Filtremos para quitar los 0 de la lista
        removers = removers + list(filter(lambda a: a<0, matches))
        matches = list(filter(lambda a: a>0, matches))
        arr = arr + matches

    #Si no ha detectado ningun precio probablemente sea que el numero esta en ingles
    matches = re.findall('-?(?:\d+?\,?)(?:\d*\.\d{2})0?(?:\s|€)', data)
    matches = [element.replace("€", "") for element in matches] #Eliminamos el símbolo de €
    #print(f"DEBUG: <{filename}> : \n\r{matches}\n\r")
    matches = [float(parse_decimal(d, locale="en_US")) for d in matches]
        # Filtramos para quitar los 0 de la lista
    if matches:
        removers = removers + list(filter(lambda a: a<0, matches))
        matches = list(filter(lambda a: a>0, matches))
        arr = arr + matches

    for el in removers:
        if abs(el) in arr:
            arr.remove(abs(el))
    maximum = max(arr)
    # Devolvemos la lista de todos los precios encontrados y el del máximo
    return (arr, maximum)

def getAllpossibleIVAConfigs(IVAOPTIONS : list, allPrices : list, total: float) -> list:
    #utilizamos la generator function de combinaciones
    allPrices = allPrices + [0] * len(IVAOPTIONS)
    #combinationsIterator es un generador de combinaciones de los precios. hora veremos si alguna combinación es o no factible
    combinationsIterator = itertools.combinations(allPrices, len(IVAOPTIONS))
    # numpy conversion cache
    IVAOPTIONSNP = np.array(IVAOPTIONS)
    possibleIVAConfigs = []
    for combination in combinationsIterator:
        if np.dot(IVAOPTIONSNP, np.array(combination)) == total:
            possibleIVAConfigs.append()
    return possibleIVAConfigs


if __name__ == "__main__":
    listaprec = [6.0, 468.0, 10.0, 20.0, 10.0, 40.0, 4.06, 316.68, 0.02, 1.62, 6.0, 468.0, 10.0, 20.0, 10.0, 40.0, 316.68, 31.67, 348.35]
    IVAOPTIONS = [0, 0.04, 0.1, 0.105, 0.106, 0.21]

    possible = getAllpossibleIVAConfigs(IVAOPTIONS, listaprec, 468.0)
    print(possible)
    pass