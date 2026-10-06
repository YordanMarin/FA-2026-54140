dolar = 3.78
euro = 4.2
soles = 0

def dolares()->float:
    return soles/dolar

def euros()->float:
    return soles/euro

print("BIENVENIDO AL SISTEMA DE CONVERSIÓN DE DOLARES Y EUROS")

while True:
    soles= float(input("\nIngrese el monto en soles: "))

    print("\nMonto en dolares: ",round(dolares(),2))
    print("MOnto en euros: ", round(euros(),2))

    conti = input("\n¿Desea continuar? (presione y): ")
    if conti != "y": break
