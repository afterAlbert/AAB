import pandas as pd

libreria = pd.read_csv("data/datos_libros.csv")

print("A.A.B\nAPLICACION ADMINISTRATIVA PARA BIBLIOTECAS")

# 1. Se piden datos del libro

titulo = input("Ingresa el titulo:")
autor = input("Ingresa el autor:")
anio = input("Ingresa el año de publicacion:")
lugar = input("Ingresa lugar de edicion:")
editorial = input("Ingresa el nombre de la editorial:")
no_edicion = input("Ingresa numero de edicion:")
# 2. Se consigue el último ID en el dataframe

ultimo_id = libreria["ID"].iloc[-1]
id_int = int(ultimo_id[3:])
nuevo_id = f"BJG{id_int+1:04d}"

# 3. Se crea un diccionario con el nuevo libro

nuevo_libro = {"ID" : nuevo_id, "TITULO" : titulo, "AUTOR" : autor, "AÑO" : anio, "LUGAR" : lugar, "EDITORIAL" : editorial, "No EDICION" : no_edicion}

# 4. Añade el libro al dataframe

libreria = pd.concat([libreria, pd.DataFrame([nuevo_libro])], ignore_index=True)

# 5. Guarda la información en el archivo CSV

libreria.to_csv("data/datos_libros.csv", index=False)
print(libreria)

print("Libro cargado con éxito")