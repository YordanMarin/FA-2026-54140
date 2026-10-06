def suma(a,b)->None:
    print("\nLa suma es: ",a+b)

def resta(a,b)->None:
    print("\nLa resta es: ",a-b)

def multi(a,b)->None:
    print("\nLa multiplicación es: ",a*b)

def divi(a,b)->None:
    if b != 0: print("\nLa divión es: ",a/b)
    else: print("\nError. No se puede dividir entre 0.")

def menu()->None:
    print("BIENVENIDOS AL SISTEMA DE CALCULADORA BÁSICA\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División\n")

while True:

    menu()
    opc = int(input("Ingrese una opción: "))

    if opc >0 and opc <5:
        a = int(input("\nIngrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

    match opc:
        case 1: suma(a,b)
        case 2: resta(a,b)
        case 3: multi(a,b)
        case 4: divi(a,b)
        case _: print("\nOpción no válida.")

    conti = input("\n¿Desea continuar? (presione y): ")
    if conti != "y": break

