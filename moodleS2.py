
# Lista donde se guardarán los productos como diccionarios
inventary = []

# Variable para mantener activo el ciclo principal del menú
follow  = True

# Variable para almacenar subtotales temporales
subtotal = 0

# Variable para confirmar salida
exitt = ""

# Ciclo principal del menú
while follow:
    # Opciones disponibles
    print("1.agregar producto:")
    print("2. mostrar inventario")
    print("3. calcualar estadisticas")
    print("4. salir")

    # Solicita al usuario elegir una opción
    option = int(input("Selecciona una opcion por favor: "))
  
    # Opción 1: Agregar productos al inventario
    if option == 1: 
        # Permite agregar varios productos seguidos
        while True:
            namep = input("ingrese el nombre del producto: ")
            price = float(input("ingrese el precio del producto: "))
            amount = int(input("ingrese la cantidad de productos: "))

            # Se crea un diccionario con la información del producto
            keep = {"nombre" :namep,"precio" :price,"cantidad" :amount }    

            # Se agrega el producto al inventario
            inventary.append(keep)

            # Pregunta si se desea agregar otro producto
            continuar=input("deseas continuar: "  )
            if continuar != "si":
                break
                
    # Opción 2: Mostrar el inventario completo
    elif  option == 2:
        # Verifica si el inventario está vacío
        if not inventary:
            print("el inventario esta vacio")

        print("tu inventario es")
        # Recorre y muestra cada producto almacenado
        for keep in inventary:
            name = keep ["nombre"]
            costs = keep ["precio"]
            products = keep ["cantidad"]
            print("----------------------------------------------------------")
            print (f"nombre:{name} | precio:{costs} | cantidad: { products} ")
            print("--------------------------------------------------------------")
     
    # Opción 3: Calcular estadísticas
    elif option == 3:
        total = 0
        # Calcula subtotales por producto
        for keep in inventary:
            costs = keep ["precio"]
            products = keep ["cantidad"]

            subtotal =  products*costs
            print("---------------------------------")
            print(f"el valor de cada producto es: ${subtotal}")
            print("---------------------------------------------")
        
        # Pregunta si se desea calcular el valor total del inventario
        calcular = input("quieres calcular el valor total del inventario si/no: ")
        if calcular == "si":
                for keep in inventary: 
                    costs = keep ["precio"]
                    products = keep ["cantidad"]
                    total +=  products * costs   
                print("----------------------------------------------")
                print(f"EL COSTO TOTAL ES: ${total}") 
                print("---------------------------------------")

    # Opción 4: Salir del programa
    elif option == 4:
        exitt = input("deseas salir del programa si/no: ")
        if exitt == "si":
            print("has salido con exito del programa")
            follow = False 

    # Si el usuario ingresa una opción no válida
    else:
        print("opcion no valida intente nuevamente")   

# Comentario final:
# Esta semana se trabajó la creación de un menú interactivo usando ciclos,
# diccionarios, listas, manejo de entradas y cálculos básicos.
