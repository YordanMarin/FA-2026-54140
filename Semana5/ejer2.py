lado1 = int(input("Ingrese lado 1 del triángulo: "))
lado2 = int(input("Ingrese lado 2 del triángulo: "))
lado3 = int(input("Ingrese lado 3 del triángulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("\nEquilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("\nIsósceles")
else:
    print("\nEscaleno")