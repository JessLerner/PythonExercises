class Coche():
	def __init__(self):
		self.puertas=4
	def nroPuertas(self):
		self.puertas+=1
		return self.puertas

miCoche=Coche()
miCoche.nroPuertas()
print("El coche tiene",miCoche.puertas,"puertas")
