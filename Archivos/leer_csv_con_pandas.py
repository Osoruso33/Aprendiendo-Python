import pandas as pd

# LEYENDO LA TABLA (CSV)
df = pd.read_csv("archivos\\texto.csv")

# IMPRIMIENDO LA TABLA (CSV)
print(df)

# EXTRAYENDO LOS DATOS DE LA COLUMNA NOMBRES
nombres = df["Nombre"]
