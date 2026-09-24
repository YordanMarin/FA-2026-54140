fi = int(input("Ingrese la cantidad de filas: "))
c = int(input("Ingrese la cantidad de columnas: "))
print()
i=0
while i < fi:
    j = 1
    while  j < c:
        print("*", end=" ")
        j+=1
    print()
    i+=1
