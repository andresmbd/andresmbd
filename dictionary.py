# C 
def crear (diccionario:dict):
    nombre = input("Ingrese el nombre: ").capitalize()
    apellido = input("Ingrese el apellido: ").capitalize()
    edad = int(input("Ingrese la edad: "))

    nuevo = input("ingrese el nuevo id: ").capitalize()
    diccionario[nuevo] = {"nombre" : nombre, "apellido" : apellido, "edad" : edad}
    return diccionario
# R
def mostrar(diccionario:dict):
    for clave, valor in diccionario.items():
        print(clave, "|", valor)

def buscar(diccionario:dict):
    busqueda_id  = input("Ingrese el id del estudiante: ").capitalize()
    encontrado = None

    for clave , valor in diccionario.items():
        if clave == busqueda_id:
            encontrado = clave
    if encontrado:
        print(valor)
        print("Encontrado")
    else:
        print("No encontrado")

# U
def actualizar (diccioanario:int):
    campos_validos = ["nombre", "apellido", "edad"]
    clave = input("Ingrese el id: ").capitalize()
    campo = input("Qué quieres cambiar?(Nombre/Apellido/Edad): ").lower()
    nuevo_valor = input("Ingrese el nuevo valor: ")

    estudiante = diccioanario.get(clave)

    if estudiante:
        if campo not in campos_validos:
            print("Campo invalido")
            
        elif campo == "edad":
            if nuevo_valor.isdigit():
                diccioanario[clave][campo] = int(nuevo_valor)
            else:
                print("Edad debe ser un numero")
        else:
            diccioanario[clave][campo] = nuevo_valor.capitalize()
    else:
        print("Id no encontrado")

    return diccioanario

    

# D
def eliminar(diccionario:dict):
    clave = input("Elimine el registro del estudinte por id: ").capitalize()
    eliminado = diccionario.pop(clave, "no existe")

    print("Registro eliminado",eliminado)

    return diccionario



    
estudiantes = {
    "A001" : {"nombre" : "Diego",
              "apellido" : "Villa",
              "edad" : 20 },
    "A002" : {"nombre" : "Mariah",
              "apellido" : "Rodiguez",
              "edad" : 18}
              }
print(estudiantes)
# estudiantes["A002"]["nacionalidad"] = "ecuatoriana"
# print(estudiantes)

op = ""
while op != "0":
    op = input("\nSeleccione la acción hacer:\n" \
                "0. Salir\n" \
                "1. Crear\n" \
                "2. Mostrar\n" \
                "3. Buscar\n" \
                "4. Eliminar\n" \
                "5. Actualizar\n" \
                "-> ")
    if op == "0":
        op = "0"
    elif op == "1":
        estudiantes = crear(estudiantes)
    elif op == "2":
        mostrar(estudiantes)
    elif op == "3":
        buscar(estudiantes)
    elif op == "4":
        estudiantes = eliminar(estudiantes)
    elif op == "5":
        estudiantes = actualizar(estudiantes)
    else:
        print("Opción invalida, ingresa el numero")