
numeros = [1,3,2,45,5,6,7,8,9,10,11,22,44,32,45,48]

# UNA FUNCIÓN LAMBDA CREA UNA VARIABLE ANONIMA (QUE NO TIENE NOMBRE)
multipicar_por_dos = lambda x : x*2

# CREANDO UNA FUNCION COMUN APRA SABER SI ES PAR O NO
def es_par(num):
    if (num%2==0):
        return True

# USANDO FILTER CON UNA FUNCIÓN COMUN (FILTRA TODOS LOS VALORES TRUE DE UN ITERABLE)
numeros_pares = list(filter(es_par,numeros))
numeros_pares.sort()
print(numeros_pares)

# LO MISMO PERO CON LAMBDA
pairs = list(filter(lambda numero:numero%2 == 0, numeros))
print(pairs)