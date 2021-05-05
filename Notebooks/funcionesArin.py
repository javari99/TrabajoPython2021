#Funciones de Arin
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
            if x + y == target:
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
    

def sumaIVAS(arr: list, target: float) -> list:
    matches = []
    IVAVALUES = [0, 0.04, 0.1, 0.105, 0.106, 0.21]
    pass


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
    #Recogemos el precio total de la factura
    matches = re.findall('(?:\d+?\.?)(?:\d*\,\d{2})0?(?:\s|€)', data)
    matches = [element.replace("€", "") for element in matches] #Eliminamos el símbolo de €
    #convertimos a numeros y luego filtramos el maximo
    matches = [float(parse_decimal(d, locale="es_ES")) for d in matches]
    arr = []
    if matches:
        # Filtremos para quitar los 0 de la lista
        matches = list(filter(lambda a: a>0, matches))
        arr = arr + matches

    #Si no ha detectado ningun precio probablemente sea que el numero esta en ingles
    matches = re.findall('(?:\d+?\,?)(?:\d*\.\d{2})0?(?:\s|€)', data)
    matches = [element.replace("€", "") for element in matches] #Eliminamos el símbolo de €
    #print(f"DEBUG: <{filename}> : \n\r{matches}\n\r")
    matches = [float(parse_decimal(d, locale="en_US")) for d in matches]
        # Filtramos para quitar los 0 de la lista
    if matches:
        matches = list(filter(lambda a: a>0, matches))
        arr = arr + matches

    maximum = max(arr)
    # Devolvemos la lista de todos los precios encontrados y el del máximo
    return (arr, maximum)

def getAllpossibleIVAConfigs(IVAOPTIONS : list, allPrices : list) -> list:
    pass

if __name__ == "__main__":
    pass