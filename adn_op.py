def calcular_contenido_de_GC(cad_Adn): # En esta función se calcula el contenido GC en cadena de ADN 

    num_t_basesg = cad_Adn.count('G')  # Cuenta el número de bases G 

    num_t_basesc = cad_Adn.count('C') # Cuenta el número de bases C 

    total_bases_sec = len(cad_Adn)  # Calcula el número total de bases 

    porc_gc = ((num_t_basesg + num_t_basesc) / total_bases_sec) * 100 # Calcula el porcentaje de contenido de GC

    return porc_gc  # Devuelve el porcentaje de contenido de GC


def resumen_de_secuencia_de_ADN(cad_Adn): # Esta función genera un resumen de la secuancia de ADN 

    resumen = {}  # Diccionario que almacena el resumen de bases y porcentajes

    # Recorre cada base en la cadena de ADN
    for base in "ATCG":
        count_base = cad_Adn.count(base)
        porcentaje = (count_base / len(cad_Adn)) * 100
        resumen[base] = porcentaje
    return resumen  # Devuelve el resumen de secuencia de ADN


def secuencia_mas_larga(cad_Adn): # Función que encuentra la secuencia más larga de bases

    # Variables que almacenan la secuencia más larga y longitud
    secuencia_max = ''
    longitud_max = 0
    for i in range(len(cad_Adn)):
        secuencia = cad_Adn[i]

        # Busca la secuencia más larga
        for j in range(i + 1, len(cad_Adn)):
            if cad_Adn[j] == cad_Adn[i]:
                secuencia += cad_Adn[j]
            else:
                break
        if len(secuencia) > longitud_max:
            longitud_max = len(secuencia)
            secuencia_max = secuencia
    return secuencia_max, longitud_max # Devuelve la secuencia más larga 


def porcentaje_de_similitud(secuencia1, secuencia2): # Función que calcula el porcentaje de similitud entre dos secuencias de ADN
    num_bases_iden = sum(1 for base1, base2 in zip(secuencia1, secuencia2) if base1 == base2)
    sim_porc = (num_bases_iden / len(secuencia1)) * 100
    return sim_porc  # Devuelve el porcentaje de similitud
