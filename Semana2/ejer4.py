print("BIENVENIDOS AL SISTEMA DE CÁLCULOS DE ÁREAS\n")
print(" --------------- Menú de opciones ---------------")
print("|            1. Cuadrado                         |")
print("|            2. Rectángulo                       |")
print("|            3. Triángulo                        |")
print("|            4. Círculo                          |")
print(" ------------------------------------------------")

opc = int(input("\nIngrese una opción: "))

match opc:
    case 1: 
        l = int(input("\nIngrese lado del cuadrado: "))
        ac = l*l
        print("\nEl área del cuadrado es ",ac)
    case 2:
        b = int(input("\nIngrese la base del rectángulo: "))
        h = int(input("Ingrese la altura del rectángulo: "))
        ar = b*h
        print("\nEl área del rectángulo es ",ar)
    case 3:
        b = int(input("\nIngrese la base del triángulo: "))
        h = int(input("Ingrese la altura del triángulo: "))
        at = (b*h)/2
        print("\nEl área del triángulo es ",at)
    case 4:
        import math
        r = int(input("Ingrese el radio del círculo: "))
        ac = math.pi * (r**2)
        print("\nEl área del círculo es ",ac)
    case _: print("\nOpción no válida.!")