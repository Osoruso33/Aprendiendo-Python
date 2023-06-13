animales = {"perro","gato","hamster","pez"} # UN CONJUNTO
razas = ["husky siberiano","persa","rusa","dorada"] # UNA LISTA
numeros = (11,44,66,33,44,55) # UNA TUPLA

# RECORRIENDO (ITERANDO) UN ELEMENTO
for animal in animales:
    print(f"El animal es {animal}")

print("----------------------")

# RECORRIENDO (ITERANDO) VARIOS ELEMENTOS A LA VEZ (SE DEBE USAR ZIP)
for animal,raza in zip(animales,razas):
    print(f"Pero es un {animal} de raza {raza}")

print("----------------------")

# EJECUTAR NUMEROS CON ELEMENTOS
for num in range(10,20):
    print(f"El numero asignado es: {num}")

print("----------------------")

# FORMA CORRECTA DE RECORRER UN ELEMENTO CON SU INDICE
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    
print("----------------------")

# USANDO EL ELSE
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("Se acabo el ultimo bucle")