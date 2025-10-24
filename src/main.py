import pandas as pd

libreria = pd.read_csv("data/datos_libros.csv")

print("A.A.B\n APLICACION ADMINISTRATIVA PARA BIBLIOTECAS")

# 1. Se piden datos del libro

titulo = input("ingresa el titulo:")
autor = input("ingresa el autor:")
anio = input("ingresa el año de publicacion:")
editorial = input("ingresa el nombre de la editorial:")

# 2. Se consigue el último ID en el dataframe

ultimo_id = libreria["ID"].iloc[-1]
id_int = int(ultimo_id[2:])
nuevo_id = f"LG{id_int+1:04d}"

# 3. Se crea un diccionario con el nuevo libro

nuevo_libro = {"ID" : nuevo_id, "TITULO" : titulo, "AUTOR" : autor, "AÑO" : anio, "EDITORIAL" : editorial}

# 4. Añade el libro al dataframe

libreria = pd.concat([libreria, pd.DataFrame([nuevo_libro])], ignore_index=True)

# 5. Guarda la información en el archivo CSV

libreria.to_csv("data/datos_libros.csv", index=False)
print(libreria)

print("Libro cargado con éxito")