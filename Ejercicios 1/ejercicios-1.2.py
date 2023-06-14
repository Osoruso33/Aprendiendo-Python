# INPUT DE ENTRADA
frase = input("Dime algo y te digo cuanto tardarías en decirlo: ")

# SEPARANDO LAS PALABRAS POR CADENAS DIFERENTES
palabras_separadas = frase.split(" ")

# CONTANDO LAS PALABRAS SEPARADAS
recuento = len(palabras_separadas)

# PASANDO LAS PALABRAS A SEGUNDOS (TENIENDO EN CUENTA QUE 2 PALABRAS EQUIVALEN A 1 SEGUNDO)
duracion_de_frase = recuento / 2

# PASANDOLO A MINUTOS DIVIDIENDOLO ENTRE 60 Y HACIENDOLO INTEGRO
minutos = int(duracion_de_frase / 60)

# HACIENDO LOS SEGUNDOS RESTANTES DE EL MINUTO
decimas_de_minutos = minutos * 60
segundos = duracion_de_frase - decimas_de_minutos

# SENTENCIA IF QUE DICE QUE SI ES MAYOR O IGUAL A 60 (UN MINUTO) VAS A QUEJARSE SI NO PUES TE LO DICE SIN QUEJARSE
if duracion_de_frase >= 60:
    print(f"Tampoco quería un testamento pero bueno, dijiste {recuento} palabras y tardarías {minutos} minutos y {int(segundos)} segundos");
else:
    print(f"Dijiste {recuento} palabras y tardarías {segundos} segundos")
