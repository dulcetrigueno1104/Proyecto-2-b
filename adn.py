#Curso: Pensamiento Computacional
#Sección: 11
#Autor: Dulce Daniela Trigueño Velásquez
#Carnet: 1247524
#Ingeniera: Damaris Campos
#Objetivo: Mejorar el análisis de la información recopilada mediante el uso eficiente de funciones, ciclos, módulos y diccionarios en el contexto del análisis de datos de ADN
#Entrada: Solicitar al usuario que ingrese las opciones que desea ejecutar y calcular a través del menú de opciones Estas opciones incluyen el registro de sujetos de prueba,cadenas de ADN, cálculo del contenido de GC, resúmenes de secuencias de ADN, identificación de la secuencia más larga, cálculo del porcentaje de similitud entre secuencias, y resumen de los sujetos de prueba y losdatos de ADN
#Salida: Devolver los resultados de las operaciones realizadas, incluyendo el contenido de GC, resúmenes de secuencias de ADN, secuencias más largas encontradas, porcentajes de similitud entre secuencias, y resúmenes de los sujetos de prueba y datos de ADN registrados





import adn_op

sujetos_de_prueba = []  # Lista para almacenar los sujetos de prueba y cadenas de ADN

# Función para registrar al sujeto de prueba
def registrar_sujeto_de_prueba(): 
    nom_sujeto = input("Ingrese el nombre completo del sujeto de prueba: ")
     # Verificación de que el nombre tenga dos palabras  
    if len(nom_sujeto.split()) < 2:
        print("El nombre debe tener de al menos dos palabras.")
        return
    sujetos_de_prueba.append((nom_sujeto, "")) # Agrega el sujeto de prueba a la lista con una cadena de ADN vacía

# Función que busca un sujeto de prueba por nombre
def buscar_sujeto(nombre):
    # Recorre la lista de sujetos de prueba para encontrar el nombre
    for sujeto in sujetos_de_prueba:
        if sujeto[0] == nombre:
            return sujeto
    return None # Retorna None cuando no se encuentre al sujeto 


# Función para ingresar la cadena de ADN para el sujeto de prueba
def ingresar_cadena_de_ADN():
    nom_sujeto = input("Ingrese el nombre completo del sujeto de prueba: ")
    sujeto = buscar_sujeto(nom_sujeto)

     # Verificar si el sujeto existe
    if not sujeto:
        print("El sujeto de prueba no existe.")
        return
    cad_Adn = input("Ingrese la cadena de ADN (debe contener solamente A, T, C, o G): ")

     # Verificar que la cadena de ADN tenga como mínimo 13 caracteres y tengan (A, T, C, G)
    if len(cad_Adn) < 13 or not all(base in 'ATCG' for base in cad_Adn):
        print("La cadena de ADN debe tener al menos 13 caracteres y contener solo bases A, T, C, o G.")
        return
     # Actualización de la cadena de ADN del sujeto de prueba
    index = sujetos_de_prueba.index(sujeto)
    sujetos_de_prueba[index] = (nom_sujeto, cad_Adn)


def calcular_contenido_de_GC(): # Función que calcula el contenido de GC en la cadena de ADN del sujeto de prueba
    nom_sujeto = input("Ingrese el nombre completo del sujeto de prueba: ")
    sujeto = buscar_sujeto(nom_sujeto)

    # Verifica si el sujeto de prueba existe
    if not sujeto:
        print("El sujeto de prueba no existe.")
        return
    cad_Adn = sujeto[1]
    
    # Verifica si el sujeto de prueba tiene una cadena de ADN ya registrada
    if not cad_Adn:
        print("El sujeto de prueba no tiene una cadena de ADN registrada.")
        return
    
    # Calcula el contenido de GC utilizando la función de adn_op
    porc_gc = adn_op.calcular_contenido_de_GC(cad_Adn)
    print(f"El contenido de GC de {nom_sujeto} es: {porc_gc:.2f}%")


def resumen_de_secuencia_de_ADN(): # Función que muestra el resumen de secuencia de ADN del sujeto de prueba
    nom_sujeto = input("Ingrese el nombre completo del sujeto de prueba: ")
    sujeto = buscar_sujeto(nom_sujeto)

    # Vuelve a verificar si el sujeto de prueba existe
    if not sujeto:
        print("El sujeto de prueba no existe.")
        return
    cad_Adn = sujeto[1]

    # Verifica si el sujeto de prueba tiene una cadena de ADN ya registrada
    if not cad_Adn:
        print("El sujeto de prueba no tiene una cadena de ADN registrada.")
        return
    
    # Se obtiene el resumen de la secuencia de ADN utilizando adn_op
    resumen = adn_op.resumen_de_secuencia_de_ADN(cad_Adn)
    print(f"Resumen de la secuencia de ADN de {nom_sujeto}:")
    for base, porcentaje in resumen.items():
        print(f"{base}: {porcentaje:.2f}%")


def secuencia_mas_larga(): # Función que encuentra la secuencia más larga la base en la cadena de ADN 

    nom_sujeto = input("Ingrese el nombre del sujeto de prueba: ")
    sujeto = buscar_sujeto(nom_sujeto)
    if not sujeto:
        print("Sujeto de prueba no existente")
        return
    cad_Adn = sujeto[1]
    if not cad_Adn:
        print("El sujeto de prueba no tiene una cadena de ADN registrada")
        return
    secuencia_max, longitud_max = adn_op.secuencia_mas_larga(cad_Adn)
    print(f"Secuencia más larga de {nom_sujeto}: {secuencia_max}, longitud: {longitud_max}")


def porcentaje_de_similitud():# Función para calcular el porcentaje de similitud entre las cadenas de ADN de dos sujetos de prueba

    nom_sujeto1 = input("Ingrese el nombre del primer sujeto de prueba: ")
    nom_sujeto2 = input("Ingrese el nombre del segundo sujeto de prueba: ")
    sujeto1 = buscar_sujeto(nom_sujeto1)
    sujeto2 = buscar_sujeto(nom_sujeto2)
    if not sujeto1 or not sujeto2:
        print("Error, uno o más sujetos de prueba no existen")
        return
    secuencia1 = sujeto1[1]
    secuencia2 = sujeto2[1]
    if not secuencia1 or not secuencia2:
        print("Uno o más sujetos de prueba no tienen una cadena de ADN ya registrada")
        return
    
    # Calcula el porcentaje de similitud con adn_op
    sim_porc = adn_op.porcentaje_de_similitud(secuencia1, secuencia2)
    print(f"Porcentaje de similitud entre {nom_sujeto1} y {nom_sujeto2}: {sim_porc:.2f}%")


def resumen_de_sujetos_de_prueba(): # Función que muestra el resumen de todos los sujetos de prueba registrados y sus cadenas de ADN

    print("Resumen de sujetos de prueba:")
    for nom_sujeto, cad_Adn in sujetos_de_prueba:
        print(f"{nom_sujeto}: {cad_Adn}")


def adn(): # Función que muestra el menú de opciones 

    while True:
        print("Menú:")
        print("1. Registrar sujetos de prueba")
        print("2. Ingresar cadena de ADN")
        print("3. Contenido de GC")
        print("4. Resumen de secuencia de ADN")
        print("5. Secuencia más larga")
        print("6. Porcentaje de similitud")
        print("7. Resumen de sujetos de prueba")
        print("8. Salir")

        op = input("Ingrese la opción que desea ejecutar: ")

        if op == "1":
            registrar_sujeto_de_prueba()
        elif op == "2":
            ingresar_cadena_de_ADN()
        elif op == "3":
            calcular_contenido_de_GC()
        elif op == "4":
            resumen_de_secuencia_de_ADN()
        elif op == "5":
            secuencia_mas_larga()
        elif op == "6":
            porcentaje_de_similitud()
        elif op == "7":
            resumen_de_sujetos_de_prueba()
        elif op == "8":
            print("Hasta pronto...")
            
        else:
            print("Opción no válida, intente de nuevo")



adn()
