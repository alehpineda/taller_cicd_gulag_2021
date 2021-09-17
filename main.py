def suma(x, y):
    """
    Esta funcion devuelve la suma de dos numeros
    """
    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise TypeError


def resta(x, y):
    """
    Esta funcion devuelve la resta de dos numeros
    """
    return x - y
