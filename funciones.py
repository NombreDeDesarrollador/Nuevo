contactos = []

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo = validar_correo()
    contacto = {"nombre":nombre, "telefono":telefono, "correo":correo}
    contactos.append(contacto)
    print("CONTACTO AGREGADO!")

def opcion_2():
    if len(contactos)==0:
        print("No existen contactos... ")
    else:
        print("LISTA DE CONTACTOS.")
        for c in contactos:
            print(f"NOMBRE:,{c['nombre']}")
            print(f"TELÉFONO:,{c['telefono']}")
            print(f"CORREO:,{c['correo']}")

def opcion_3():
    if len(contactos)==0:
        print("No existen contactos... ")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")+".csv"
        import csv
        with open(nombre_archivo, "w", newline="")as archivo:
            escritor = csv.DictWriter(archivo, ["nombre", "telefono", "correo"])
            escritor.writerows(contactos)

def opcion_4():
    print("SHAOLIN SOCCER")
    exit()

def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print("ERROR")

def validar_telefono():
    while True:
        try:
            tel = int(input("Ingrese telefono: "))
            if len(str(tel))==9 and str(tel)[0]==9:
                return tel
            else:
                print("ERROR")
        except:
            print("Error")


def validar_correo():
    while True:
        cor = input("Ingrese correo: ")
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip)>=13:
            return cor
        else:
            print("ERROR")