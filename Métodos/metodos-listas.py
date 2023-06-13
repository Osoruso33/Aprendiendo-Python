primeraLista = ["Juan","Las Palmas de GC","Pedro",36]
listaDeInt = [6,24,1,34,64,2,14]

# Len cuenta los elementos de la lista
len(primeraLista)

# Append agrega un elemento a la lista
primeraLista.append(True)

# Insert agrega un elemento a la lista en un indice especifico
primeraLista.insert(2, "C/Tomas morales, 24")

# Extend agrega varios elementos a una lista
primeraLista.extend([False, 1.87])

# Pop elimina un elemento de la lista por su indice
primeraLista.pop(5)

# Remove elimina un elemento por su valor
primeraLista.remove(False)

# Sort coloca en orden ascendente solo las listas de Int
listaDeInt.sort()
# si ponemos reverse: true entre los parentesis ordena de forma descendente

# Reverse invierte los elementos de la lista
primeraLista.reverse()

# Index encuentra un elemento de la lista y devuelve su indice
listaDeInt.index(6)

print(primeraLista)
print(listaDeInt)

# Clear elimina la lista entera
primeraLista.clear()

print(primeraLista)