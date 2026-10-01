p = i = 0

while True:
    num = int(input("Ingrese un número (negativo para finalizar): "))

    if num > 0:
        if(num % 2 == 0):
            p+=1
        else:
            i+=1
    else: 
        break

print("\nCantidad de pares: ", p)
print("Cantidad de impares: ",i)
