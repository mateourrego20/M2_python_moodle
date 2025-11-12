
# Lista donde se guardarán los productos como diccionarios
inventario = []

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
    opcion = int(input("Selecciona una opcion por favor: "))
  
    # Opción 1: Agregar productos al inventario
    if opcion == 1: 
        # Permite agregar varios productos seguidos
        while True:
            nombre = input("ingrese el nombre del producto: ")
            precio = float(input("ingrese el precio del producto: "))
            cantidad = int(input("ingrese la cantidad de productos: "))

            # Se crea un diccionario con la información del producto
            guardar  = {"nombre" :nombre,"precio" :precio,"cantidad" :cantidad }    

            # Se agrega el producto al inventario
            inventario.append(guardar)

            # Pregunta si se desea agregar otro producto
            continuar=input("deseas continuar: "  )
            if continuar != "si":
                break
                
    # Opción 2: Mostrar el inventario completo
    elif  opcion == 2:
        # Verifica si el inventario está vacío
        if not inventario:
            print("el inventario esta vacio")

        print("tu inventario es")
        # Recorre y muestra cada producto almacenado
        for guardar in inventario:
            name = guardar ["nombre"]
            costo = guardar ["precio"]
            productos = guardar ["cantidad"]
            print("----------------------------------------------------------")
            print (f"nombre:{name} | precio:{costo} | cantidad: {productos} ")
            print("--------------------------------------------------------------")
     
    # Opción 3: Calcular estadísticas
    elif opcion == 3:
        total = 0
        # Calcula subtotales por producto
        for guardar in inventario:
            costo = guardar ["precio"]
            productos = guardar ["cantidad"]

            subtotal = productos*costo
            print("---------------------------------")
            print(f"el valor de cada producto es: ${subtotal}")
            print("---------------------------------------------")
        
        # Pregunta si se desea calcular el valor total del inventario
        calcular = input("quieres calcular el valor total del inventario si/no: ")
        if calcular == "si":
                for guardar in inventario: 
                    costo = guardar ["precio"]
                    productos = guardar ["cantidad"]
                    total += productos * costo   
                print("----------------------------------------------")
                print(f"EL COSTO TOTAL ES: ${total}") 
                print("---------------------------------------")

    # Opción 4: Salir del programa
    elif opcion== 4:
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
