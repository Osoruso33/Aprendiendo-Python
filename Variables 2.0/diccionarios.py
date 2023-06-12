# CREANDO DICCIONARIOS CON dict()
diccionario = dict(nombre="Francisco",apellido="Rodríguez")

# LAS TUPLAS PUEDEN SER CLAVES (LAS LISTAS NO, PERO FROZENSETS SI)
diccionario2 = {("Dalmata", "Raza") : "Perro"}

# CREANDO DICCIONARIOS CON fromkeys()
diccionario3 = dict.fromkeys(["nombre","apellido"])

# CAMBIANDO EL VALOR POR DEFECTO DE fromkeys()
diccionario3 = dict.fromkeys(["nombre","apellido"],"N/A")