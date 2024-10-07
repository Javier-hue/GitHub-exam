def mostrar_menu(): 
    print("\menu")
    print("1. Ver elementos") 
    print("2. Agregar elementos")
    print("3. Modificar elemento")
    print("4. Eliminar elemento")
    print("5. Salir ") 

def agregar_elementos(lista):
    print("\nArreglo actual: ", lista)
    elemento = input("Ingresa el elemto: ")
    lista.append(elemento)
    print("Nuevo arreglo:", lista)

def modificar_elemento(lista):
    print("\Arreglo actual:", lista)
    indice = int(input("Ingresa el indice del elemento: "))
    nuevo_valor = input("Ingresa el nuevo valor: ")
    lista[indice] = nuevo_valor
    print("Arreglo modificado", lista)

def  eliminar_elemento(lista): 
    print("\nArreglo actual:", lista)
    indice = int(input("Ingresa el indice que eliminara: "))
    lista.pop(indice)
    print("Arreglo despues de eliminar:", lista)

if __name__ == "__main__": 
    mi_lista = []
    while True: 
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1": 
            print("\nElementos de la lista:", mi_lista)
        elif opcion == "2": 
            agregar_elementos(mi_lista)
        elif opcion == "3":
            modificar_elemento(mi_lista)
        elif opcion == "4":
            eliminar_elemento(mi_lista)
        elif opcion == "5":
            print("Bye :D ")
            break
        else: 
            print("Opcion incorrecta")
