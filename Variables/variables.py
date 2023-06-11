# Variables: objetos que pueden variar, los puedes crear del nombre y valor que tu quieras

# Estoy escribiendo en notación de tipo camelCase
# (Primera letra en minuscula palabras unidas y el inicio de cada  palabra nueva en mayuscula)
numeroDeCoches = 20

# Las variables son modificables

numeroDeCoches = 30

# Hay varios tipos de iguales

# Igual normal (=)
numeroDeCoches = 50

# Igual operado (+=, -=, *= /=)
# Este suma, resta, divide y multiplica el valor anterior con el proporcionado

numeroDeCoches += 10

# CONCATENACIÓN con f-strings: Unir strings

# print es el comando para imprimir en la consola
print(f"Hay {numeroDeCoches} coches")

# Convertir un tipo de dato en otro
# se pone el tipo de dato a cambiar como una funcion "Int("72")"

# Como pueden ver el Int se ha unido como un string en el debug (darle al f5) y esto es por que es un f string
# que va en llaves (es una variable que se convierte en string)

# siempre hay que poner las variables en llaves y una f antes del string de print

# BORRAR UN VALOR EN UNA VARIABLE

del numeroDeCoches 

# Operadores

# in / not in (Operador de pertenencia): sirve para  encontrar algo en una variable
presentacion = "Soy Pedro vivo en alemania"

print("alemania" in presentacion)
# la consola dice true por que si esta alemania en el texto

print("Pedro" not in presentacion)
# Dice false por que si hay un pedro en el texto

# Tambien se puede definir una variable en snake_case (separar las palabras por guiones bajos)
prueba_de_snake_case = "Usen la que les sea mas cómodo"