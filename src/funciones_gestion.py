#src/funciones_gestion.py

# Funcion de ingreso de libros
def ingresar_libro(inv):
    
    # Funcion para guardar la información en un archivo CSV
    def guardar_ingreso(ingreso, inv, nl):
        # Si la varible de ingreso es positiva, entonces se carga el libro
        if ingreso == True:
            # Añade libro al DataFrame
            inv = pd.concat([inv, pd.DataFrame([nl])], ignore_index=True)
            
            # Guarda la información en el archivo CSV
            inv.to_csv("data/inventario.csv", index=False)
            # Muestra el inventario actual
            print(inv)

            print("Libro cargado con éxito")
        else:
            # Se cancela la escritura del CSV
            print("No se ha cargado ningún libro")
    
    # 1. Se inician las variables: variable de ID, diccionario con info. del libro y la variable de ingreso
    ultimo_id = inv["ID"].iloc[-1]
    id_int = int(ultimo_id[3:])
    nuevo_id = f"BJG{id_int+1:04d}"

    nuevo_libro = {"ID" : nuevo_id, "TITULO" : False, "AUTOR" : False, "AÑO" : False, "LUGAR" : False, "EDITORIAL" : False, "No EDICION" : False}
    
    ingreso = True
    # 2. Convierte en una lista las claves del diccionario y empieza el bucle salteando la clave ID
    for i in list(nuevo_libro.keys())[1:]:
        # 3. Se añade un valor a cada clave o se cancela mediante el comando "fin"
        nuevo_libro[i] = input(f"Ingresa {i} o escribe 'fin' para salir:")
        if nuevo_libro[i] == "fin":
            # 3.1 Se cancela el ingreso y se rompe el bucle
            ingreso = False
            break
    # 4. Se 
    guardar_ingreso(ingreso, inv, nuevo_libro)
