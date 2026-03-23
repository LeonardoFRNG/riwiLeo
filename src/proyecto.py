#lista inventario vacia
inventario = []

#funcion para agregar productos
def agregar_producto ():
    # #pedir nombre(no necesita validacion)
    nombre = input("Ingrese el nombre del producto: ")
    
    #pedir precio (necesita validacion)
    while True:
        try:
            precio = float(input("Ingrese el precio de su producto: "))
            break
        except:
            print("Precio invalido, intente de nuevo.")
            
    #pedir cantidad (necesita validacion)
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except:
            print("Cantidad invalida, intente de nuevo.")
            
    #crear diccionario y guardar
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"{producto} agregado correctamente. ")
    
#Funcion para mostar el inventario
def mostrar_productos ():
    #len lo usamos para obtener la longitud op numero de elementos de un objeto, como listas, tuplas, o diccionarios, aca rectificamos que si la lista esta vacia salte unmensaje al ussuario
    if len (inventario) == 0:
        print("El inventario esta vacio. ")
        #aca recorremos toda la lista
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        
def estadisticas_producto():
    #len lo usamos para obtener la longitud op numero de elementos de un objeto, como listas, tuplas, o diccionarios, aca rectificamos que si la lista esta vacia salte unmensaje al ussuario
    if len (inventario) == 0:
        print("El inventario esta vacio. ")
        return
    #iniciamos la variable total en 0
    total = 0
    #recorremos la lista para calcular el total
    for producto in inventario:
        total += producto['cantidad'] * producto['precio']
    #creamos una variable que ttome el total de los productos en inventario
    cantidad_productos = len(inventario)
    #imprimimos
    print(f"Total de los productos registrados: {cantidad_productos}")
    print(f"Valor total del inventario: {total}")
    
    
#while que se ejecuta hasta que el user elija salir
while True:
    print("====MENU INVENTARIO====\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")
    
    opcion = input("Elige una opcion:\n")
    
    if opcion == "1":
        agregar_producto()              
    elif opcion == "2":
        mostrar_productos()
        
    elif opcion == "3":
        estadisticas_producto()
        
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    
    else:
        print("opcion invalida, intente de nuevo")
    