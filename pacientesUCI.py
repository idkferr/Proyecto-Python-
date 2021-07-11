import matplotlib.pyplot as plt

datosUCI = []
regiones = []
cod_region = ["15","1","2","3","4","5","13","6","7","16","8","9","14","10","11","12"]


"""
  # Método que carga los datos del CSV en lista datosUCI
  # entradas: archivo csv
  # salida: lista con datos del csv
"""
def carga_datos():
	with open("UCI_std.csv","r",encoding="utf-8") as f:
		for i in f.readlines():
			fila = i.split(",")
			datosUCI.append(fila)
			if fila[0] not in regiones:
				regiones.append(fila[0])
	regiones.pop(0)
	datosUCI.pop(0)   # eliminamos primera fila ya que son los títulos del archivo csv

"""
  # Método inicial que muestra el menú del software
  # entradas: usuario selecciona opción
  # salida: depende de selección de usuario 
"""
def main():
	carga_datos()
	print("\nBienvenido al sistema de gestión de pacientes UCI nacional\nseleccione una de las siguientes opciones")
	print("(1) Mostrar gráfico de pacientes UCI de las últimas dos semanas de una región")
	print("(2) Generar análisis estadístico por región")
	print("(3) Listar código de las regiones")
	print("(4) Ver regiones con registro max() & min() de pacientes UCI")
	print("(5) Cerrar programa")
	accion = input("\nIngrese acción: ")
	if accion=='1':
		opcion1()
	if accion=='2':
		# llamar método analytics() para generar estadística y consultar si volver o cerrar el programa
		print("soy la opción 2")
		volver()
	if accion=='3':
		listarCodigoRegiones()
		volver()
	if accion=='4':
		UCImaxYmin()
		volver()
	if accion=='5':
		# cierra el programa
		exit()
	else:
		print("\n\nERROR: Seleccione una opción válida\n\n")
		main()

"""
  # Submenú de la opción 1 "Mostrar gráfico de pacientes UCI de las últimas dos semanas"
  # entradas: usuario selecciona opción, después selecciona una región
  # salida: muestra gráfico según opción ingresada de las últimas 2 semanas
"""
def opcion1():
	print("\nHa seleccionado la opción de Mostrar gráfico de pacientes UCI de las últimas dos semanas\nfavor ingrese una de las siguientes opciones")
	print("(a) Pacientes NO ACUMULATIVOS")
	print("(b) Pacientes ACUMULATIVOS")
	print("(c) volver al menú principal")
	accion = input("\nIngrese acción: ").upper()
	if accion=='A':
		graficaNoAcumulativo()
		volver()

	if accion=='B':
		graficaAcumulativo()
		volver()

	if accion=='C':
		main()

"""
  # comentar
"""
def graficaNoAcumulativo():
	seleccion = input("\nPara generar la gráfica NO ACUMULATIVA, seleccione el nombre o el código de la región: ")
	# tenemos que validar que lo ingresado sea efectivamente algo válido, de otra forma, solicitamos nuevamente el ingreso de la región
	valida_region(seleccion, 'graficaNoAcumulativo')
	# si pasó la validación del método valida_region(), entonces graficamos:
	print(datosUCI[0]) 



"""
  # comentar
"""
def graficaAcumulativo():
	seleccion = input("\nPara generar la gráfica ACUMULATIVA, seleccione el nombre o el código de la región: ")
	# tenemos que validar que lo ingresado sea efectivamente algo válido, de otra forma, solicitamos nuevamente el ingreso de la región
	valida_region(seleccion, 'graficaAcumulativo')
	# si pasó la validación del método valida_region(), entonces graficamos:
	print(datosUCI[0])



"""
  # valida que la región ingresada, ya sea por su nombre o código, exista
  # entrada: input usuario (region/código)
  # entrada: string para volver al submenú de donde estaba
  # salida: mensaje de validación correcta | mensaje de error y vuelta a submenú
"""
def valida_region(seleccion, way_back):
	if seleccion in regiones or seleccion in cod_region:
		print("\n\nVALIDACIÓN CORRECTA: " + seleccion)
	else:
		print("\n\nERROR: Región no se encuentra en sistema, verifique ortografía o mayúsculas\n\n")
		if way_back == "graficaNoAcumulativo":
			graficaNoAcumulativo()
		else:
			graficaAcumulativo()


"""
  # Listar nombre de las regiones con su respectivo código
  # salida tabla con regiones y códigos
"""
def listarCodigoRegiones():
	print("\nCódigo | Región")
	print("-------------------------")
	for idx,value in enumerate(regiones):
		if len(cod_region[idx]) == 1:
			print(" " + cod_region[idx] + "     | " + value)
		else:
			print(cod_region[idx] + "     | " + value)









""" # Sumamos los pacientes UCI por región y día."""				
def suma_de_Datos (regiones):
	total_datos = []
	for region in regiones:
		suma_datos = 0
		for i in datosUCI:
			if region == i[0]: 
				suma_datos += int(i[4])
		total_datos.append(suma_datos)
	return total_datos

"""#Se hace una comparacion de los resultados y se muestra cual es el maximo y minimo de pacientes UCI dentro  de las regiones."""
def UCImaxYmin():
	datos = suma_de_Datos (regiones)
	print (datos)
	print (regiones)
	print("\nRegión      |    Pacientes UCI")
	print("--------------------------------")

	minimo = min(datos)
	maximo = max(datos)
	region_max = regiones[datos.index(maximo)]
	region_min = regiones[datos.index(minimo)]
	
	print (region_min + "\t"+ "\t" + str(minimo))
	print (region_max + "\t" + str(maximo))
	


  # volver al menú principal
  # entradas: usuario selecciona opción S/N
  # salida 'S': vuelve al menú principal
  # salida 'N': cierra el programa

def volver():
	accion = input("\n¿Volver? (s/n): ").upper()

	while accion not in ["S","N"]:
		print("\n\nERROR: Seleccione una opción válida\n\n")
		accion = input("\n¿Volver? (s/n): ").upper()

	if accion == 'S':
		main()
	else:
		print("\n\nALERTA: El programa se cerrará, hasta pronto...\n\n")
		exit()

# Iniciamos el programa llamando al menu principal
if __name__ == '__main__':
    main()