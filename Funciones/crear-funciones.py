
print("----------------------")

# CREANDO UNA FUNCIÓN SIMPLE
def saludar():
    print("Hola adrián mi loco")

# EJECUTAR LA FUNCIÓN SIMPLE
saludar()

# CREANDO UNA FUNCIÓN COMPLEJA
def saludar2(nombre):
    print(f"Hola {nombre}, ¿Que tal?")
    
# EJECUTANDO UNA FUNCIÓN COMPLEJA
saludar2("Abel")

print("----------------------")

# DEVOLVIENDO SOLO UN VALOR QUE SE PUEDE ASIGNAR A UNA VARIABLE
def numero(number):
    num_final = round(number * 7 / 2)
    return num_final

# CREANDO UNA VARIABLE CON EL VALOR RESULTANTE DE LA FUNCION
number = numero(6)

print(number)
