import matplotlib.pyplot as plt

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
		# llamar método analytics() para generar estadística y consultar si volver o cerrar el programa
		print("soy la opción 2")
		volver()
	if accion=='3':
		# llamar método listarCodigoRegiones()
		print("soy la opción 3")
		volver()
	if accion=='4':
		# llamar método UCImaxYmin()
		print("soy la opción 4")
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
		# mostrar grafico, llamando a def graficaNoAcumulativo()
		#este print es solo para ustedes, lo deben borrar
		print('Concultamos la región a mostrar por número o código y luego\nMostramos gráfico No Acumulativo y después preguntamos a usuario si quiere volver al menu principal')
		volver()

	if accion=='B':
		# mostrar grafico, llamando a def graficaAcumulativo()
		#este print es solo para ustedes, lo deben borrar
		print('Concultamos la región a mostrar por número o código y luego\nMostramos gráfico Acumulativo y después preguntamos a usuario si quiere volver al menu principal')
		volver()

	if accion=='C':
		main()


"""
  # comentar
"""
def graficaNoAcumulativo():
	print('aqui muestro la grafica no acumulativa')
	break

"""
  # comentar
"""
def graficaAcumulativo():
	break

"""
  # comentar
"""
def analytics():
	break

"""
  # comentar
"""
def listarCodigoRegiones():
	break

"""
  # comentar
"""
def UCImaxYmin():
	break



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
if __name__ == '__main__':
    main()