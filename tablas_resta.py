#Mostar Tablas de Restar

def generar_tablas_resta(max_num_tabla):
    for num_tabla in range(0,max_num_tabla +1):
      print("Tabla #", num_tabla)
      for linea in range (0,10):
        print("\t", num_tabla, "-", linea, "=", num_tabla - linea)
    print("\n")