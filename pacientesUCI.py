import statistics
import matplotlib.pyplot as plt

datosUCI = []
regiones = []
cod_region = []

"""
  # Método que carga los datos del CSV en lista datosUCI
  # entradas: archivo csv
  # salida: lista con datos del csv
"""
def carga_datos():
	with open("UCI_std.csv","r",encoding="utf-8") as f:
		for i in f.readlines():
			fila = i.split(",")
			if fila[0] != "Region":     # eliminamos primera fila ya que son los títulos del archivo csv
				datosUCI.append(fila)
				if fila[0] not in regiones:
					regiones.append(fila[0])
					regiones.append(fila[1])
					cod_region.append(fila[1])

"""
  # Método inicial que muestra el menú del software
  # entradas: usuario selecciona opción
  # salida: depende de selección de usuario 
"""
def main():
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
		analytics()
	if accion=='3':
		listarCodigoRegiones()
	if accion=='4':
		UCImaxYmin()
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
	if accion=='B':
		graficaAcumulativo()
	if accion=='C':
		main()

"""
  # Creación de gráfico pacientesUCI NO ACUMULATIVO último 14 días por región seleccionada
"""
def graficaNoAcumulativo():
	seleccion = input("\nPara generar la gráfica NO ACUMULATIVA, seleccione el nombre o el código de la región: ")
	# tenemos que validar que lo ingresado sea efectivamente algo válido, de otra forma, solicitamos nuevamente el ingreso de la región
	valida_region(seleccion, 'graficaNoAcumulativo')
	# si pasó la validación del método valida_region(), entonces graficamos:
	datos = filtro_region(seleccion)
	datos = datos[-14:]
	ejeX = []
	ejeY = []
	titulo = datos[0][0]  # nombre de la región
	for i in datos:
		ejeX.append(i[3])
		ejeY.append(int(i[4]))
	plt.title("Gráfico últimos 14 días total de pacientesUCI NO ACUMULATIVOS - región: " + titulo)
	plt.ylabel("PacientesUCI NO acumulativos")
	plt.xlabel("Fecha")
	plt.plot(ejeX,ejeY,"r")
	plt.show()
	volver()

"""
  # Creación de gráfico pacientesUCI ACUMULATIVOS último 14 días por región seleccionada
"""
def graficaAcumulativo():
	seleccion = input("\nPara generar la gráfica ACUMULATIVA, seleccione el nombre o el código de la región: ")
	# tenemos que validar que lo ingresado sea efectivamente algo válido, de otra forma, solicitamos nuevamente el ingreso de la región
	valida_region(seleccion, 'graficaAcumulativo')
	# si pasó la validación del método valida_region(), entonces graficamos:
	datos = filtro_region(seleccion)
	datos = datos[-14:]
	ejeX = []
	ejeY = []
	acumulativo = 0
	titulo = datos[0][0]  # nombre de la región
	for i in datos:
		acumulativo += int(i[4])
		ejeX.append(i[3])
		ejeY.append(acumulativo)
	plt.title("Gráfico últimos 14 días total de pacientesUCI ACUMULATIVOS - región: " + titulo)
	plt.ylabel("PacientesUCI acumulativos")
	plt.xlabel("Fecha")
	plt.plot(ejeX,ejeY,"r")
	plt.show()
	volver()

"""
	# Análisis de los datos
	# Entrada: selección de región
	# Salida: Promedio pacientesUCI por día, población total, promedio pacientesUCI por total de población, Mediana y Moda de pacientesUCI en la región
"""
def analytics():
	seleccion = input("\nSeleccione el nombre o el código de la región: ")
	# tenemos que validar que lo ingresado sea efectivamente algo válido, de otra forma, solicitamos nuevamente el ingreso de la región
	valida_region(seleccion, 'analytics')
	print("\nSe está cargando un análisis estadístico de la región seleccionada:")
	print("   +++ " + region_nombre(seleccion) +" +++\n\n")
	data = analisis(seleccion)
	pob = int(poblacion_region(seleccion))
	promedio = statistics.mean(data)
	porcentaje = float(promedio/pob)
	mediana = statistics.median(data)
	moda = statistics.mode(data)
	print("El promedio de pacientes UCI diarios en la región es de:", '{0:.3f}'.format(promedio))
	print("Considerando que la región tiene un total de " + str(pob) + " habitantes, podemos interpretar que ")
	print("el porcentaje de pacientes UCI promedio de la región por la totalidad de habitantes es de:", '{0:.15f}'.format(porcentaje))
	print("Otro dato interesante de observar es la mediana, que equivale a: " + str(mediana))
	print("Y la moda (o valor más reiterativo) es: " + str(moda))
	volver()

"""
  # Listar nombre de las regiones con su respectivo código
  # salida tabla con regiones y códigos
"""
def listarCodigoRegiones():
	print("\nCódigo | Región")
	print("-------------------------")
	for i in cod_region:
		if len(i) == 1:
			print(" " + i + "     | " + region_nombre(i))
		else:
			print(i + "     | " + region_nombre(i))
	volver()

"""
	# Sumatoria de acumulativo de pacientes UCI por región, se efectúa comparación de los resultados
	# y se muestra cuál es el máximo y mínimo de pacientes UCI dentro de las regiones.
	# Entrada: -
	# Salida: región min() y max() de pacientesUCI según datos históricos
"""
def UCImaxYmin():
	datos = suma_pacientesUCI_region()
	print("\nRegión      |    Pacientes UCI")
	print("--------------------------------")
	minimo = min(datos)
	maximo = max(datos)
	region_max = region_nombre(cod_region[datos.index(maximo)])
	region_min = region_nombre(cod_region[datos.index(minimo)])

	print(region_min + "\t"+ "\t" + str(minimo))
	print(region_max + "\t" + str(maximo))
	volver()



"""
  # valida que la región ingresada, ya sea por su nombre o código, exista
  # entrada: input usuario (region/código)
  # entrada: string para volver al submenú de donde estaba
  # salida: mensaje de validación correcta | mensaje de error y vuelta a submenú
"""
def valida_region(seleccion, way_back):
	if seleccion in regiones:
		print("\n\nVALIDACIÓN CORRECTA: " + seleccion)
	else:
		print("\n\nERROR: Región no se encuentra en sistema, verifique ortografía o mayúsculas\n\n")
		if way_back == "graficaNoAcumulativo":
			graficaNoAcumulativo()
		elif way_back == "analytics":
			analytics()
		else:
			graficaAcumulativo()

"""
  # Concentramos datos según región seleccionada
  # Entrada: región seleccionada por el usuario
  # Salida: datos CSV exclusivos de la región seleccionada por el usuario
"""
def filtro_region(seleccion):
	filtro = []
	for i in datosUCI:
		if seleccion in i:
			filtro.append(i)
	return filtro

"""
	# Colectamos solo los datos de una región en particular
	# Entrada: región selectada por usuario
	# Salida: datos históricos de esa región
"""
def analisis(seleccion):
	analisis = []
	for i in datosUCI:
		if seleccion in i:
			num = int(i[4])
			analisis.append(num)
	return analisis

"""
	# Entrega la población de una región específica
	# Entrada: región selectada por usuario
	# Salida: número de habitantes de una región previamente seleccionada
"""
def poblacion_region(seleccion):
	pob = ""
	for i in datosUCI:
		if seleccion in i:
			pob = i[2]
	return pob

"""
	# Entrega nombre de la región según código
	# Entrada: código numérico de la región
	# Salida: nombre de la región
"""
def region_nombre(seleccion):
	for i in datosUCI:
		if seleccion in i:
			return i[0]

"""
	# Sumamos los pacientes UCI por región y día.
"""
def suma_pacientesUCI_region():
	total_datos = []
	for cod in cod_region:
		suma_datos = 0
		for fila in datosUCI:
			if cod == fila[1]:
				suma_datos += int(fila[4])
		total_datos.append(suma_datos)
	return total_datos

"""
  # volver al menú principal
  # entradas: usuario selecciona opción S/N
  # salida 'S': vuelve al menú principal
  # salida 'N': cierra el programa
"""
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
carga_datos()
if __name__ == '__main__':
  main()