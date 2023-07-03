# CON WITH, CUANDO SE ACABAN LAS ACCIONES EN LA IDENTACIÓN CIERRA EL ARCHIVO
with open("archivos\\texto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())
    print("Despues de este texto se cerrará el archivo")
