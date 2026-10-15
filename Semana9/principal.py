from cuadrado import cuadrado
from rectangulo import rectangulo
c = cuadrado()

def menu():
    print("BIENVENIDO AL SISTEMA DE CÁLCULOS DE ÁREAS Y PERÍMETROS\n")
    print("********** Menú de opciones *********")
    print("* 1. Cuadrado                       *")
    print("* 2. Rectangulo                     *")
    print("* 3. Triángulo                      *")
    print("* 4. Trapecio                       *")
    print("* 0. Salir                          *")
    print("*************************************")

menu()
while True:
    while True:
        try:
            opc = int(input("\nIngrese una opción: "))
        except ValueError:
            opc = -1
        if 0 <= opc <= 4:
            break
        print("Opción no válida. Ingrese un número entre 0 y 4.")

    match opc:
        case 0: exit()
        case 1: 
            while True:
                try:
                    l = float(input("\nIngrese el lado del cuadrado: "))
                    if l > 0: break
                    else: print("Error. Ingrese un número positivo.")
                except ValueError:
                    print("Error. Ingrese solo números")
            print("\nCuadrado: ")
            c.area(l)
            c.perimetro(l)

        case 2:
            r = rectangulo()
            print()
            print("Area: ", r.area())
            print("Perimetro: ", r.perimetro())

    while True:
        conti = input("\n¿Desea continar? (s/n): ").lower().strip()
        if conti in("s", "n"):
            break
        print("Opción no válida, Ingrese solo (s o n).")

    if conti == "n": break


