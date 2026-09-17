edad = int(input("Ingresa la edad: "))

if edad >= 18:
    print("Es elegible para votar")

    if edad >= 25:
        print("También es elegible para ser candidato.")
    else:
        print("No es eleible para ser candidato.")
else:
    print("NO es elegible para votar ni ser candidato.")
    
