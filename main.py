import os
import globales 
import ventas_aleatorias

os.system("cls")


def menu_general():
    while True:
        os.system("cls")
        print ("menu general")
        print("")
        print("1. asignar monto aleatorio ")
        print("2. ver estadisticas")
        print("3. salir del programa")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            os.system("cls")
            ventas_aleatorias.generar_ventas_aleatorias()
            print("ventas aleatorias asignadas.")
            input()

        elif opcion ==2:
            os.system("cls")
            


