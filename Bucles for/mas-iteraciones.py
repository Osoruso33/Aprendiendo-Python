
frutas = ["platano","manzana","ciruela","pera","melón","naranja","granada","melocoton"]
cadena = "Hola dalto"
numeros = [2,4,8,16]

# ITERANDO UNA LISTA REMOVIENDO UN VALOR
for fruta in frutas:
    if fruta == "granada":
        # CONTINUE OMITE UNA ACCIÓN
        continue
    print(f"Me voy a comer una {fruta}")
    
print("----------------------")
    
# ITERANDO UNA LISTA TERMINANDO EL BUCLE (SI HAY UN ELSE TAMPOCO VA A EJECUTARSE)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "melón":
        # BREAK CORTA EL BUCLE
        break

print("----------------------")

# ITERANDO UNA STRING
for letra in cadena:
    print(letra)

print("----------------------")

# CREANDO UN FOR EN UNA SOLA LINEA DE CODIGO
numero_duplicados = [x*2 for x in numeros]
print(numero_duplicados)