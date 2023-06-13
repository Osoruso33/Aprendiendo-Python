
numeros = [4,7,3,8,9,21]

# FUNCIONES BUILT-IN:

print("----------------------")

# ENCUENTRA EL NUMERO MAYOR DE UNA LISTA
print(f"El numero mas alto de la lista es: {max(numeros)}")

# ENCUENTRA EL NUMERO MENOR DE UNA LISTA
print(f"El numero mas bajo de la lista es: {min(numeros)}")

print("----------------------")
    
# REDONDEAR A 2 DECIMALES (EN EL SEGUNDO VALOR SE PONEN LAS DECIMALES QUE SE QUIEREN MANTENER (POR DEFECTO VIENE 0))
print(f"El numero redondeado a las centésimas es: {round(12.593129302919203,2)}")

print("----------------------")

# RETORNA FALSE -> 0, VACÍO, FALSE, NINGUNO \ TRUE -> DISTINTO DE 0, TRUE, CADENA, DATOS NO VACÍOS
print(bool(12))

# RETORNA TRUE SI TODOS LOS VALORES SON VERDADEROS (PERO CON ITERABLES)
print(all(numeros))

print("----------------------")

# SUMA TODOS
print(sum(numeros))
