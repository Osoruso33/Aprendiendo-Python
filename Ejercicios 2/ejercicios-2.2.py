# CREAR UNA FUNCION QUE NOS DEVUELVA LOS NUMEROS PRIMOS ENTRE 0 Y EL ARGUMENTO QUE PASAMOS

# CREANDO UNA FUNCION QUE REVISA LOS NUMEROS PRIMOS
def buscar_numeros_primos():
    numeros_primos = [1,]
    
    # AQUI SE CREA LA LISTA QUE DEBE SER DIVIDIDA
    for number in range(2, pregunta_numeros + 1):
        
        # UNA VARIABLE BOOLEANA QUE CONTROLA SI ES PRIMO O NO
        es_primo = True
        
        # AQUI CREA LA LISTA DE DIVISORES
        for divisor in range(2, int(number/2) + 1):
            
            # AQUI REVISAMOS SI ES PRIMO
            if number % divisor == 0:
                
                # SI NO LO ES LO MARCA COMO FALSO Y ROMPE EL BUCLE
                es_primo = False
                break
            
        # SI ES PRIMO LO AÑADE
        if es_primo:
            numeros_primos.append(number)
            
    # SORTED HACE LO MISMO QUE SORT PERO QUITA LOS REPETIDOS
    numeros_primos_sin_repetir = sorted(numeros_primos)
    
    # SI EL RECUENTO DE NUMEROS PRIMOS ES 1 (VALOR INICIAL) RESPONDA ESTO
    if len(numeros_primos_sin_repetir) == 1:
        print(f"Solo es 1 el numero primo entre 0 y {pregunta_numeros}")
        
    # SI NO RESPONDE ESTO
    else:
        print(f"Los numeros primos del 0 al {pregunta_numeros} son: {numeros_primos_sin_repetir}")
        
# HACEMOS LA PREGUNTA PARA SABER EL NUMERO
pregunta_numeros = int(input("Dime un numero y te digo los primos de el 0 a ese numero: "))

# EJECUTANDO LA FUNCION
buscar_numeros_primos()