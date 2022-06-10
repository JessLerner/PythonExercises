print ("Verificacion de acceso")

edad_usuario=int(input("Introduce tu edad: "))

if edad_usuario>100 or edad_usuario<0:
	print("Edad incorrecta")
elif edad_usuario<18:
	print("No Puede ingresar")
else:
	print("Puede ingresar")