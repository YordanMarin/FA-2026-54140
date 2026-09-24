try:
    num = int(input("Ingrese el número de la tabla (1-12): "))
    while num <=0 or num > 12:
        num = int(input("Error. Ingrese el número de la tabla (1-12): "))

    i=1

    while i <= 12:
        print(f"{num} x {i} = {num*i}")
        i+=1

except ValueError:
    print("Solo se permiten números.")