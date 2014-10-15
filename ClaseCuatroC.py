

def longitud_str(fn):
    def wrapped(*args):
        return len(fn())
    return wrapped

def ingresoStr():
    str = raw_input("Ingrese Stream: ")
    print str
    return str
