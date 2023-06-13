# FALTO EL PROFE Y VAN A HACER UNA CLASE LOS ALUMNOS

# PEDIR EL NOMBRE Y EDAD DE LOS COMPAÑEROS QUE VINIERON HOY A CLASE

# CREANDO UNA FUNCÍON QUE CREA UNA FICHA (TUPLA) DENTRO DE UNA LISTA CON LA EDAD Y EL NOMBRE DE CADA ALUMNO A PARTIR DE UN INPUT
def obtener_compañeros(cantidad):
    compañeros = []
    for students in range(cantidad_de_compañeros):
        nombre = input("¿Tu nombre?: ")
        edad = input("¿Edad?: ")
        compañero = (nombre,edad)
        compañeros.append(compañero)
    # AQUI SE LES DA REVERSA PARA QUE TOME EN CUENTA DESPUES EN EL SORT POR EL NUMERO Y N>O EL ORDEN ALFABETICO
    compañeros.reverse()
    return compañeros

# LE DECIMOS AL ORDENADOR QUE CREE UN INPUT QUE SE CONVERTIRA EN UN INT PARA SABER LA CANTIDAD DE COMPAÑEROS
cantidad_de_compañeros = int(input("¿Cuantos son hoy en clase?: "))

# UTILIZANDO LA PREVIA FUNCIÓN CON EL PARAMETRO COMO EL INPUT ANTERIOR CREANDO UNA VARIABLE DE TIPO LISTA DE LAS FICHAS DE LOS COMPAÑEROS
fichas_de_compañeros = obtener_compañeros(cantidad_de_compañeros)

# COLOCANDO EN ORDEN ASCENDENTE LAS FICHAS POR EDAD
fichas_de_compañeros.sort()

# DESEMPAQUETANDO LA TUPLA Y PIDENDO EL MAXIMO Y EL MINIMO DE CADA VARIABLE
profesor,edad_de_profesor = max(fichas_de_compañeros)
asistente,edad_de_asistente = min(fichas_de_compañeros)

print("--------------------")

# LOS COMPAÑEROS QUE HAY EN EL AULA
print(f"Hay {cantidad_de_compañeros} alumnos en el aula")

print("--------------------")

# UN BUCLE FOR PARA DECIR CADA COMPAÑERO SEPARADO DE LA LISTA
print("Los alumnos son:")
for compañero in fichas_de_compañeros:
    print(f"{compañero}")
    
print("--------------------")

# QUIEN ESEL PROFESOR Y QUIEN ES EL ASISTENTE
print(f"El profesor es {profesor}")
print(f"El asistente es {asistente}")