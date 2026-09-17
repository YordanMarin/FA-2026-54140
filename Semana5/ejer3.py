n = int(input("Ingresar la cantidad de números: "))

suma_pares = 0

print("\nLista de números:")
for i in range(1,n+1):
    print(i)
    if i%2==0:
        suma_pares += i


print("\nSuma de pares: ",suma_pares)