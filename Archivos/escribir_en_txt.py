with open("archivos\\texto.txt","w",encoding="UTF-8") as archivo:
    # SOBREESCRIBIENDO TODO EL TEXTO
    # archivo.write("TE JURO QUE ES BUENO")
    
    # AGREGANDO TEXTO POR LINEAS (LA \n ES PARA PASAR DE LINEA)
    archivo.writelines(["Hola, ¿Como te encuentras?\n", "Ya estoy recuperado de...\n", "LA FIEBRE DEL SEA\n"])
    