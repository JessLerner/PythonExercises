def numeroprimo():
	numero= int(input('Introduce un número entero: '))
	primo=False

	if numero > 1
		for i in range(2,numero):
			if numero% i== 0 :
				print("a")
				primo=False
				break
			else:
				primo=True
		return primo
	else:
		return (f"Lo siento, el número {numero} NO ES PRIMO. Los números primos son mayores que 1")
  
  
respuesta=numeroprimo()

if respuesta==True:
	print("El numero es Primo")
elif respuesta==False:
	print("El numero no es primo")
else:
	print(respuesta)
