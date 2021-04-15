#Funciones de Arin

def twoSum(arr : list, target : float) -> list:
    """[summary]
    Busca todos los pares de números de la lista que suman al target
    Args:
        arr (list): [Lista de números]
        target (float): [description]

    Returns:
        list: [description]
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
    que no vayan a ser el precio final
    Args:
        arr (list): [Lista de numeros por los que se buscan el target]
        target (float): [El número deseado que encontrar con la suma]

    Returns:
        tuple: [Los dos candidatos para el precio]
    """
    candidates = twoSum(arr,target)
    #Buscamos el máximo de todos, que probablemente sea la base imponible
    max = -1
    for i in candidates:
        for el in i:
            max = el if el > max else max
    
    for i in candidates:
        if max in i:
            return i
    



def sumaivas(arr: list, target: float) -> list:
    matches = []
    IVAVALUES = [0, 0.04, 0.1, 0.105, 0.106, 0.21]
    pass