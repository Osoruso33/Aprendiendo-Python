# Matrices

# Listas

primeraLista = ["Juan","Las Palmas de GC","Pedro",36]
print(primeraLista)
# en corchetes para elegir del 0 al infinito de la lista
print(primeraLista[2])

# Tuplas (Listas no modificables)

primeraTupla = ("Pedro","SB","Juan",34)
print(primeraTupla)

# Modificar una lista

primeraLista[1] = "Málaga"
print(primeraLista)

# Conjuntos (Sets) (Inmodificable solo reconstruible)
# reconstruible (se puede crear todo de nuevo)
# no se pueden imprimir elementos por indice y no almacenan datos duplicados

primerSet = {"Paula","Arrecife","Manolo",26}
print(primerSet)

# Diccionarios (Dicts)
primerDiccionario = {
    "Nombre" : "Manolo",
    "Residencia" : "Barcelona",
    "Amigos" : "Juan y Paula",
    "Edad" : 28
}

print(primerDiccionario["Residencia"])