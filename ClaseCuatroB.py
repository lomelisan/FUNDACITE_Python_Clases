#Decorador 2

from ClaseCuatroA import logger

@logger
def sigma(*args):
    return sum([i for i in args])
    











