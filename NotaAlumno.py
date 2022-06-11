"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def aprobado(self):
        if self.nota >= 5:
            print("Aprobado")
        else:
            print("No aprobado")

Jose=Alumno("Jose", 7)
Jose.imprimir()
Jose.aprobado()

Martin=Alumno("Martin", 3)
Martin.imprimir()
Martin.aprobado()
