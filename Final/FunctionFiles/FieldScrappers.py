import itertools
from typing import List
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



def extraerFecha_0(fech):
    o=fech.replace('-','/')
    o=o.split('/')
    fecha_final_0_aux=Logic(o)
    fecha_final_0='/'.join(fecha_final_0_aux)
    return fecha_final_0

def extraerFecha_1(fech): 
    a=fech.split('-')
    meses = {'ene': '01', 'feb' : '02', 'mar' : '03', "abr" : '04', 'may':'05', 'jun': '06', 'jul':'07', 'ago':'08', 'set':'09', 'oct':'10','nov':'11', 'dic':'12' }
    a[1]=meses[a[1]]
    fecha_final_aux=Logic(a)
    fecha_final='/'.join(fecha_final_aux)
    return fecha_final

def extraerFecha_2(fech):
    b=fech.split(' ')
    Meses = {'enero': '01', 'febrero' : '02', 'marzo' : '03', "abril" : '04', 'mayo':'05', 'junio': '06', 'julio':'07', 'agosto':'08', 'septiembre':'09', 'octubre':'10','noviembre':'11', 'diciembre':'12' }
    b[2]=Meses[b[2]]
    
    for i in range(2):      #Eliminar lo "de" 
     b.remove("de")
    fecha_final_2_aux=Logic(b)
    fecha_final_2='/'.join(fecha_final_2_aux)
    return fecha_final_2

def extraerFecha_3(fech):
    c=fech.split(' ')
    MESES = {'Enero': '01', 'Febrero' : '02', 'Marzo' : '03', "Abril" : '04', 'Mayo':'05', 'Junio': '06', 'Julio':'07', 'Agosto':'08', 'Septiembre':'09', 'Octubre':'10','Noviembre':'11', 'Diciembre':'12' }
    c[1]=MESES[c[1]]
    fecha_final_3_aux=Logic(c)
    fecha_final_3='/'.join(fecha_final_3_aux)
    return fecha_final_3

def Logic(dato): #Funcion para evitar resultados ilógicos.
    if float(dato[0])>31 or float(dato[1])>12 or  float(dato[2])>2025:
         vuelta=["error"]
    else:
        vuelta=dato
    return vuelta


def getAllInvoiceNumbers(inString : str):
    
    matches =  re.findall('ES-\d{3}', \
                inString)
   #facturas real y pura
    matches = matches + re.findall('(?<=FACTURA SIMPLIFICADA ).*', \
                inString)
#ticket
    matches = matches + re.findall('(?<=Número de factura).*', \
                inString)
    #prueba 1_1 y 1_2
    matches = matches + re.findall('FRO\d{11}', \
                inString)
    #prueba 5 y prueba 6
    matches = matches + re.findall('(?<=NÚMERO\n).*', \
                inString)
    #prueba 9 prueba 10 y prueba 11
    matches = matches + re.findall('(?<=FACTURA\n).*\d{4} \d{2}', \
                inString)
    #prueba1_3
    matches = matches + re.findall('(?<=FACTURA : ).*\d{4}', \
                inString)
    #prueba 
    matches = re.findall('(?<=\d{8}[A-Z]\n).*\d{3}\/\n\d{1} \d{3}', \
                inString)
    
    matches = matches + [line.replace("\n","") for line in matches7]
    #prueba 1_4
    matches = matches + re.findall('(?<=\d{2}\/\d{2}\/\d{4}\n).*\d{3}\/\d{4}', \
                inString)
    #ivanormal3 
    matches = matches + re.findall('(?<=FACTURA: ).*[A-Z]\/\d{6}', \
                inString)
    #ivalineas3
    matches = matches + re.findall('(?<=\d{2}\/\d{2}\/\d{2}\n).*\d{2}\/\d{3}', \
                inString)
    #12ocr
    matches = matches + re.findall('(?<=Factura: ).*\d', \
                inString)
    #ivalineas1?
    matches = matches + re.findall('(?<=Numero: ).*\d{3}', \
                inString)
    return matches

def getPhoneNumbers(inString : str) -> list:
    matches = re.findall('9\d \d{3} \d{2} \d{2}\s| 9\d{2} \d{6}\s| 9\d{2} \d{3} \d{3}\s| 9\d{8}\s| 9\d{2} \d{2} \d{2} \d{2}\s', \
                inString)
    matches = [line.strip().strip('\n') for line in matches]
    return matches

def getEmails(inString : str) -> list:
    matches = re.findall('(?:\w+\.)?\w+@\w+.\w+', \
                inString)
    return matches

def getAllDates(inString : str) -> list:
    
    intarr = []
    matches = re.findall('\d{1,2}[\/|-]\d{1,2}[\/|-]\d{1,4}', \
                inString)
    # F1
    if matches:
        for i in range(len(matches)):
            # Transform dates
            matches[i] = extraerFecha_0(matches[i])
        # Remove error dates
        matches = list(filter(lambda a: a!="error", matches))
        intarr += matches
    # F2
    matches = re.findall('([0-9]{1,2}-(ene|feb|mar|abr|may|jun|jul|ago|set|oct|nov|dic)-(20)?[0-9]{2,4})', \
                inString)
    if matches:
        for i in range(len(matches)):
            matches[i] = matches[i][0] #Linea para quedarnos con el primer elemento de la tupla que es la que nos intersa
            #Antes de escribir le cambiamos el formato para que quede con un formato con el que podamos meter a excel
            matches[i] = extraerFecha_1(matches[i])
        intarr += matches
    # F3
    matches = re.findall('([0-9]{1,2} (de) (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) (de) [0-9]{2,4})', \
                inString)
    if matches:
        for i in range(len(matches)):
            matches[i] = matches[i][0]#Linea para quedarnos con el primer elemento de la tupla que es la que nos intersa
            #Antes de escribir le cambiamos el formato para que quede con un formato con el que podamos meter a excel
            matches[i] = extraerFecha_2(matches[i]) 
        intarr += matches 
    # F4
    matches = re.findall('([0-9]{1,2} (Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre) [0-9]{2,4})', \
                inString)
    if matches:
        for i in range(len(matches)):
            matches[i] = matches[i][0]#laLinea para quedarnos con el primer elemento de la tupla que es  que nos intersa
            #Antes de escribir le cambiamos el formato para que quede con un formato con el que podamos meter a excel
            matches[i] = extraerFecha_3(matches[i]) 
        intarr += matches
    # Finally we convert to a set to remove duplicates and convert back to a list
    return list(set(intarr))