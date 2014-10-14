class Auto():
    """Esta clase va arrancar un auto segun su gasolina"""
    gasolina=0
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"
    
    @staticmethod
    def arrancar(gasolina):
        if gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"
            
    @staticmethod
    def moverse(gasolina):
        if gasolina > 0:
            gasolina -= 1
            print "Quedan", gasolina, "litros"
        else:
            print "No hay gasolina para moverse..."

class Helo(Auto):
                pass


