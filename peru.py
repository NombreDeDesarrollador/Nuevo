import os, time
from funciones import *

while True:
    os.system('cls')
    print("MENÚ CONTACTOS")
    print("1. Agregar contacto. ")
    print("2. Ver contactos. ")
    print("3. Exportar. ")
    print("4. SALIR. ")
    opc = int(input("INGRESE OPCIÓN: "))

    os.system('cls')
    if opc ==1:
        opcion_1()
    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3()
    else:
        opcion_4()
    time.sleep(3)