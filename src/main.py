#src/main.py

import pandas as pd
import funciones_gestion as fg

ingresar_libro = fg.ingresar_libro
# Direccion de info. de libros
direccion = "data/inventario.csv"

inventario = pd.read_csv(direccion)

#Titulo del programa en pantalla
print("A.A.B\nAPLICACION ADMINISTRATIVA PARA BIBLIOTECAS")

ingresar_libro(inventario)