print("BIENVENIDOS AL SISTEMA DE CONVERSIÓN DE DINERO\n")
print(" --------------- Menú de opciones ---------------")
print("|         1. Convertir a dolares                 |")
print("|         2. Convertir a euros                   |")
print(" ------------------------------------------------")

opc = int(input("\nIngrese una opción: "))
if opc >=1 and opc <=2:
    soles = float(input("Ingrese el monto en soles a convertir: "))

match opc:
    case 1: 
        dolares = soles/3.75
        print("Monto en dolares: $",round(dolares,2))
    case 2:
        euros = soles/4.05
        print("Monto en dolares: $",round(euros,2))
    case _: print("\nOpción no válida.!")
        