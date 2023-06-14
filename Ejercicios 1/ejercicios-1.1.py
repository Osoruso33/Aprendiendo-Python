# DATOS
otrosCursosMax = 7.0
otrosCursosMin = 2.5
otrosCursosPromedio = 4.0
esteCurso = 1.5
crudoEsteCurso = 3.5
crudoOtrosCursos = 5.0

# PRIMERA ACTIVIDAD
resultadoA1 = int(100 - esteCurso / otrosCursosMin * 100)
resultadoA2 = int(100 - esteCurso / otrosCursosMax * 100)
resultadoA3 = int(100 - esteCurso / otrosCursosPromedio * 100)
print("------------------------------------------------------")
print(f"A) 1. La diferencia entre el más rapido de los otros cursos y este curso es de {resultadoA1}% aprox.")
print(f"A) 2. La diferencia entre el más lento de los otros cursos y este es de {resultadoA2}% aprox.")
print(f"A) 3. La diferencia entre el promedio de los otros cursos y este es de {resultadoA3}% aprox.")

# SEGUNDA ACTIVIDAD
resultadoB1 = int(100 - (otrosCursosPromedio / crudoOtrosCursos * 100))
resultadoB2 = int(100 - (esteCurso / crudoEsteCurso * 100))

print("------------------------------------------------------")
print(f"B) 1. El porcentaje de material recortado de el promedio de otros cursos es de {resultadoB1}% aprox.")
print(f"B) 2. El porcentaje de material recortado de este curso es de {resultadoB2}% aprox.")

# TERCERA ACTIVIDAD
resultadoC1 = int((otrosCursosPromedio * 10) / esteCurso)
resultadoC2 = int((esteCurso * 10) / otrosCursosPromedio)

print("------------------------------------------------------")
print(f"C) 1. Ver 10 horas de este curso equivale a {resultadoC1} horas aprox. del promedio de otros cursos")
print(f"C) 2. Ver 10 horas de el promedio de otros cursos equivale a {resultadoC2} horas aprox. de este curso")
print("------------------------------------------------------")