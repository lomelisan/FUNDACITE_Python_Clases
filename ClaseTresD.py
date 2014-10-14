class Auto():
    """Clase de abstraccion"""
    gasolina=0
    def __init__(self, gasolina):
       Auto.gasolina = gasolina 
       print "Tenemos", gasolina, "litros"
       
    @classmethod
    def arrancar(cls, gasolina):
        if gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"
    
    @classmethod
    def moverse(cls, gasolina):
            if gasolina > 0:
               gasolina -= 1
               print "Quedan", gasolina, "litros"
            else:
               print "No hay gasolina para moverse..."

