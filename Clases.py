class Vehiculo:
    def __init__(self):
        color="rojo"
        ruedas=0
        puertas=0

class Coche(Vehiculo):
    velocidad=0
    Cilindrada=0
    def producto(self):
        print("el coche es color",self.color,"tiene",self.ruedas,"ruedas y",self.puertas,"puertas, su velocidad maxima es",self.velocidad,
        "y su cilindrada es",self.Cilindrada)

celta=Coche()
celta.color="negro"
celta.ruedas=4
celta.puertas=5
celta.velocidad=120
celta.Cilindrada=4
celta.producto()
