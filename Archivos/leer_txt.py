
# ABRIMOS EL ATCHIVO Y LO CONVERTIMOS EN UNA VARIABLE
archivo = open("archivos\\texto.txt")

# SOLO SE PUEDE LEER UNA VEZ EL ARCHIVO POR METODOS DE SEGURIDAD

# IMPRIMIMOS EL ARCHIVO LEEYENDOLO
# print(archivo.read())

# IMPRIMIMOS UN ARRAY CON LAS LINEAS
# print(archivo.readlines())

# IMPRIMIMOS UNA SOLA LINEA 
print(archivo.readline())

# CERRAR EL ARCHIVO
archivo.close()