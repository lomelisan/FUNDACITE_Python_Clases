#Decorador

def sigma(*args):
    return sum([i for i in args]) #Lista de comprension

def logger(fn):
    def wrapper(*args):
        for i, arg in enumerate(args):
            print "arg: %d. %d" % (i, arg)
        return fn(*args)
    return wrapper




    
    



