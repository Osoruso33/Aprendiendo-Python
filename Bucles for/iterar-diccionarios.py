diccionario = {
    "Nombre": "Diego",
    "Edad": 23,
    "IES": "IES Jaime Balmes"
}

# KEY DEVUELVE SOLO LAS CLAVES ITERADAS
for key in diccionario:
    print(f"Devolviendo las claves: {key}")
    
# FORMA CORRECTA DE ITERAR DICCIONARIOS (CON ITEMS)
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")