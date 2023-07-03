name = input("Cual es su nombre: ")
age = input("Cual es su edad: ")
job = input("Cual es su ocupación: ")
nacionality = input("Cual es su nacionalidad: ")
address = input("Cual es su localidad: ")

with open("prueba\\ficha.txt","w",encoding="UTF-8") as cuestionary:
    cuestionary.writelines([f"Nombre: {name}\n", f"Edad: {age}\n", f"Ocupación: {job}\n", f"Nacionalidad: {nacionality}\n", f"Localidad: {address}\n"])