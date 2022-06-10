"""Escribe una función que calcule el área de un triángulo,recibiendo la altura y la base como parámetros y 
otra función que calcule el área de un círculo recibiendo el radio del mismo."""

import math

def areaTriangulo(h,b):
  return (b*h)/2

def areaCirculo(radio):
  resultado=math.pi *(radio**2)
  return round(resultado,2)
