
print("----------------------")

def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, que tal {adjetivo}?"

# SE PUEDE PONER EN CUALQUIER ORDEN SIEMPRE Y CUANDO ESTE ESPECIFICADO CON LA VARIABLE
frase = frase(adjetivo = "mi lider",nombre = "Luis",apellido = "Lopez")

print(frase)

print("----------------------")

# PUEDES PONER UN VALOR PREDEFINIDO PERO PUEDES DEFINIRLO DE NUEVO (EN CASO DE QUE NO PONGAS NADA AUTOMATICAMENTE DICE TONTITO)
def frasesota(nombre,apellido,adjetivo = "tontito"):
    return f"Hola {nombre} {apellido}, que tal {adjetivo}?"

frasesita = frasesota("Luis","Lopez")

print(frasesita)