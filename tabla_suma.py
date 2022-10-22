
#definicion de funcion para tabla de sumar
def generar_tablas_suma(maximo_numero_tabla):
    for numero_tabla in range(0, maximo_numero_tabla + 1):
      print("Tabla #", numero_tabla)
      for linea in range(0,10):
        print("\t", numero_tabla, " + ", linea, " = ", numero_tabla + linea)
      print("\n")
