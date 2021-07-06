import matplotlib.pyplot as plt

def listadoRegiones():
    with open("UCI_std.csv","r",encoding="utf-8") as f:   # Abro el archivo csv con utf-8
        regionesListados = [] 
        codigoyRegionListado = []
        for i in f.readlines(): # Recorro todas las linas del archivo abierto y despues los convierto en 
            linea = i.split(",") # una lista que contiene el nombre y codigo de regiones
            regionesListados.append(linea[2])  
            codigoyRegionListado.append(linea[2])#inconcluso
            codigoyRegionListado.append(linea[3])

    return regionesListados,codigoyRegionListado # Lo devuelvo como una tupla ya que tengo una lista que ocupare para mostrar al uruario y otra
                                                # para la validacion de lo que ingrese.

def ejeX():
    with open("UCI_std.csv","r",encoding="utf-8") as f:
        fechas = []
        for i in f.readlines():
            print(i)
            linea = i.split(",")
            # for fecha in range(len(linea)-16,len(linea)-1,1): # Este for esta seccionado ya que los graficos solo toman en cuenta
                # fechas.append(linea[fecha])                  # los ultimas 14 fechas
            break                                            # El break es para para el for ya que solo existe para obtener las fechas

    DatosEjeX = []
    for i in range(7):  # Este for existe en un rango de 7 para crear la parte del eje x del grafico
        root = fechasChile[i]   # El que tendria Dia N y la fecha del dia N
        formato = "Dia " + str(i+1) + "\n" + root
        DatosEjex.append(formato)
    return DatosEjeX

def grafico(datosAGraficar,DiasGraficoEjeX,tipoDeGrafico):
    ejey = datosAGraficar
    ejex = DiasGraficoEjeX
    plt.title(tipoDeGrafico)
    plt.plot(ejex,ejey,"r")
    plt.ylabel("Contagios")
    plt.show()
    return

def filtroComuna(datoDeFiltro):
    with open("Datos.csv","r",encoding="utf-8") as f:
        filtrada = []
        for i in f.readlines():
            linea = i.split(",")
            if datoDeFiltro in linea:   # Compruebo si el datodefiltro el cual seria comuna esta en la lista para asi solo obtener las que coincidan
                filtrada = linea
    return filtrada

def datosNoAcumuladoComuna(filtrada):
    listaNoAcumulativa = []
    for i in range(len(filtrada)-8,len(filtrada)-1,1): # Este for esta en un rango para obtener los 8 ultimos datos sin contar la tasa de la lista filtrada
        listaNoAcumulativa.append(int(float(filtrada[i])-float(filtrada[i-1]))) # Esto es para obtener el primero y el segundo, luego con las resta de ambos
    return listaNoAcumulativa                                                   # me deberia dar el total de casos no acumulado ya que los datos que nos
                                                                                # entregan estan acumulados.
def datosAcumuladoComuna(filtrada):
    listaAcumulativa = []
    for i in range(len(filtrada)-8,len(filtrada)-1,1):  
        listaAcumulativa.append(int(float(filtrada[i])))    # Los transformo primero a floar ya que viene con formato de decimal y luego a integro
    return listaAcumulativa                                 # o entero, el no hacer esto daba error
    
def filtroRegion(region):
    with open("Datos.csv","r",encoding="utf-8") as f:
        filtrada = []
        for i in f.readlines():
            linea = i.split(",")
            if region in linea:   # Compruebo si el datodefiltro el cual seria region esta en la lista para asi solo obtener las que coincidan
                filtrada.append(linea)
    return filtrada

def datosGraficoRegionAcumulado(filtrada):
    listaDatosRegion = [0,0,0,0,0,0,0,0] # lista creada solo para ir sumando con los indices
    for comuna in filtrada:
        contador = 0 # es ocupado para obetener el indice de la lista donde estaran las sumas de todo
        for i in range(len(comuna)-9,len(comuna)-1,1):  # Este for obtiene 8 datos ya que son necesario 8 datos para obtener el no acumulado si es necesario
            listaDatosRegion[contador] = int(listaDatosRegion[contador] + float(comuna[i])) # voy sumando lo que ya estaba en la lista y el nuevo valor obtenido de la otra comuna
            contador += 1
        contador = 0 # reinicio valor para seguir con otra comuna

    return listaDatosRegion

def datosGraficoNoAcumuladoRegion(listaDatosRegion):
    listaNoAcumulada = []

    for i in range(1 , len(listaDatosRegion)): # Este for empieza en 1 ya que para obtener los casos totales de una region seria el valor anterior menos el nuevo
        listaNoAcumulada.append(listaDatosRegion[i] - listaDatosRegion[i-1]) # Aqui hago la operacion y la ingreso a una lista

    return listaNoAcumulada

DiasGraficoEjeX = ejeX() # Llamo a la funcion ejex para obtener el ejex de todos los graficos

tipoDeGrafico1 = "Grafico de Contagios no acumulados"
tipoDeGrafico2 = "Grafico de Contagios acumulados"

accion = 0
while accion != 3:  # Para que este siempre activo hasta que el usuario quiera salir.
    print("ingrese una opcion")
    print("(1) Region con menos pacientes en Estado UCI")
    print("(2) Region con más pacientes en Estado UCI")
    print("(3) ingrese el Codigo de la Region")
    print("(4) cerrar programa")
    accion = input("Ingrese accion: ")
    
    while accion not in ["1","2","3"]:  # Validacion para que el usuario ingrese una opcion valida
        accion = input("Ingrese accion: ")

    accion = int(accion)

    if accion == 1:
        tuplaComuna = listadoRegiones()  # Pedimos los datos de la funcion listadoComunas
        listaComunas = tuplaComuna[0]
        listaComunaImprimir = str(listaComunas)
        listaComunaImprimir = listaComunaImprimir.replace("'", "").replace("[", "").replace("]","") # Esto es solo para eliminar comillas extra que contenia las listas 
        print(listaComunaImprimir)                                                                  # y corchetes

        Comuna = input("Ingrese comuna o codigo de comuna: ")

        while Comuna not in tuplaComuna[1]: # compruebo que lo que ingresa el usuario exista en los datos que se pueden buscar
            print("Comuna no encontrada")
            Comuna = input("Ingrese comuna sin acento o codigo de comuna: ")
        
        resultado = filtroComuna(Comuna)    # Llamo a la funcion filtroComuna
        
        print("¿Que desea hacer?")
        print("(a) Mostrar un gráfico de contagiados no acumulativos de la comuna")
        print("(b) Mostrar un gráfico de contagiados acumulativos de la comuna")
        print("Los graficos se haran en base a las 7 ultimas fechas")
        graficoAccion = input("Ingrese eleccion: ")

        while graficoAccion not in ["a","b","A","B"]:  # Validacion para que el usuario ingrese una opcion valida
            graficoAccion = input("Ingrese eleccion: ")

        if graficoAccion == "a":
            datosAgraficarNoAcumulado = datosNoAcumuladoComuna(resultado)   # LLamo a la funcion de datosNoAcumulado

            grafico(datosAgraficarNoAcumulado,DiasGraficoEjeX,tipoDeGrafico1)   # Llamo a la funcion grafico ingresando las variables
        elif graficoAccion == "b":
            datosAgraficarAcumulado = datosAcumuladoComuna(resultado)   # LLamo a la funcion de datosNoAcumulado
            grafico(datosAgraficarAcumulado,DiasGraficoEjeX,tipoDeGrafico2)

    elif accion == 2:
        tuplaRegiones = listadoRegiones()   # LLamo a la funcion listado regiones

        listaRegiones = tuplaRegiones[0]    # leo el primer elemento de la tupla
        listaRegionesCodigo = tuplaRegiones[1]  # luego el segundo elemento de la tupla

        for i in range(len(listaRegiones)): #Imprimo el lista de regiones dado por la funcion para que lo vea el usuario
            print(f"-{listaRegiones[i]}")

        eleccion = input("Ingrese el numero de la Region seleccionada, Codigo de region o Nombre: ")

        while eleccion not in listaRegionesCodigo:  # Validacion de que ingrese un codigo o region valida y bien escrita.
            eleccion = input("Ingrese el numero de la Region seleccionada, Codigo de region o Nombre: ") 

        resultado = filtroRegion(eleccion)  # LLamo a la funcion filtro Region

        print("¿Que desea hacer?")
        print("(a) Mostrar un gráfico de contagiados no acumulativos de la Region")
        print("(b) Mostrar un gráfico de contagiados acumulativos de la Region")
        print("Los graficos se haran en base a las 7 ultimas fechas")
        graficoAccion = input("Ingrese eleccion: ")

        while graficoAccion not in ["a","b","A","B"]:   # While para que el usuario ingrese una opcion valida
            graficoAccion = input("Ingrese eleccion: ")

        if graficoAccion == "a":
            Datos = datosGraficoRegionAcumulado(resultado) # LLamo a la funcion datosGraficoRegionAcumulado con los datos de la funcion filtroRegion
            Datos = datosGraficoNoAcumuladoRegion(Datos)    # LLamo a la funcion datosGraficoNoAcumuladoRegion con los datos de la funcion datosGraficoRegionAcumulado
            grafico(Datos,DiasGraficoEjeX,tipoDeGrafico1)
        elif graficoAccion == "b":
            Datos = datosGraficoRegionAcumulado(resultado)
            Datos.remove(Datos[0])  # Remuevo el primer dato ya que la lista tiene 8 y son solo necesario 7, en este caso los 7 ultimos          
            grafico(Datos,DiasGraficoEjeX,tipoDeGrafico2)

    elif accion == 3:   # Creado para finalizar el programa si asi el usuario lo desea.
        print("Programa finalizado, nos vemos luego!")
        