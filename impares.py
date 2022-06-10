"""Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]"""

numInicio=int(input("Introduce el número inicial: "))
numFinal=int(input("Introduce el número final: "))

while numInicio<=numFinal:
    if numInicio%2!=0:
        print(numInicio)
    numInicio+=1