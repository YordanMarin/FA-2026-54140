anio = int(input("Ingrese el año: "))
print()
if (anio % 4 == 0 and anio % 10 != 0) or anio % 400 == 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")

if anio % 2 == 0: print("El año es par")
else: print("El año es impar")

print()