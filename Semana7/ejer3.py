opc = "n"
while opc != "s":
    i=1
    suma = 0
    num = int(input("Ingrese un número positivo: "))
    
    while i <= num:
        suma += i
        i+=1
    
    print(f"\nLa suma desde 1 hasta {num} es: {suma}")

    opc = input("\nDesea salir? (presione s): ")
print()
