cadena1 = "Hola soy Alberto"
cadena2 = "Bienvenido genio"

# dir te devuelve todos los atributos posibles a añadir en la variable
# OJO: Dir es una funcion no un metodo pero entra en este temario
dir(cadena1)

# Los metodos se colocan así
# Upper convierte todas las letras en mayúsculas
cadena1.upper()

# Lower convierte todas las letras en minusculas
cadena2.lower()

# Capitalize convierte la primera letra en mayuscula
cadena1.capitalize()

# Find es para buscar una cadena en otra cadena
# cuando no se encuentra nada devuelve -1
cadena2.find("genio")

# Index es para buscar una cadena en otra cadena
# cuando no se encuentra nada devuelve una excepcion
cadena1.index("soy")

# Isnumeric hace que si es numerico devuelve true si no devuelve false
cadena2.isnumeric()

# Isalpha hace que si es alfanumerico devuelve true si no devielve false
cadena1.isalpha()

# Count cuenta las coincidencias de la cadena que has proporcionado dentro de otra cadena
cadena2.count("a")

# Len cuenta los caracteres de una cadena
# OJO: Len es una funcion
len(cadena1)

# Startswith es para saber si empieza por el caracter que proporciones
cadena2.startswith("B")

# Endswith es lo mismo pero apra saber si termina por
cadena1.endswith("o")

# Replace reemplaza una cadena por otra
cadena2.replace("genio","maquina")

# Split separa cadenas con las cadenas que le pasemos
cadena1.split(" ")