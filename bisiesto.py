def esBisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return ("Es Bisiesto")
    else:
        return ("No es Bisiesto")
        
print(esBisiesto(int(input("Ingrese el año que desea saber si es Bisiesto: "))))
