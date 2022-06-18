"""Crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora. 
En el caso de que sean más de las 19, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo."""

import time
hora=time.localtime().tm_hour
minuto=time.localtime().tm_min

if hora>=19 and hora<=8:
	print("Puedes irte a casa")
elif hora==18:
	print("Faltan ",59-minuto,"minutos para que puedas irte")
else:
	print("Faltan ",18-hora,"horas y",59-minuto," minutos para que puedas irte")
