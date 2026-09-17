n = int(input("Ingresar la cantidad de números: "))
pares = impares = ceros = 0
print()

for i in range(1,n+1):
    num = int(input(f"Ingrese número {i}: "))

    if  num ==0:
        ceros += 1
    elif num %2 == 0:
        pares +=1
    else:
        impares+=1

print("\nCantidad de pares: ",pares)
print("Cantidad de impares: ", impares)
print("Cantidad de ceros: ", ceros)