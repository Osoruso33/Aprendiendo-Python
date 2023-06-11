primerDiccionario = {
    "Nombre" : "Manolo",
    "Residencia" : "Barcelona",
    "Amigos" : "Juan y Paula",
    "Edad" : 28
}

# Keys nos devuelve las claves y nos sirve para iterar el dict
primerDiccionario.keys()

# Get nos da el elemento de la clave proporcionada (si no existe esa clave te aparece none)
primerDiccionario.get("Nombre")

# Clear elimina todo del diccionario
# primerDiccionario.clear()

# Pop elimina un elemento de el diccionario
primerDiccionario.pop("Amigos")

# Items itera el diccionario (lo recorre) pero ahora mismo no lo podemos hacer (se explica en bucles)