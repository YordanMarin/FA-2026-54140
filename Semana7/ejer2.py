import random

print("BIENVENIDOS AL JUEGO ADIVINADOR\n")
print("-"*65)
print(" Instrucciones: ")
print(" 1. Ud. debe de adivinar el número entre 1 y 20.")
print(" 2. Se le proporcionara una pista por cada intento erroneo.")
print(" 3. Ud. tiene solo 3 intentos.")
print("-"*65)

intentos = 3
a = random.randint(1,20)

while intentos > 0: 
    num = int(input(f"Intento {intentos}. Ingrese el número a adivinar: "))

    if num == a:
        print("Adivinaste el número.")
        break
    else:
        if num < a:
            print("El número debe de ser mayor.\n")
        else: 
            print("El número debe de ser menor.\n")
        intentos-=1
else:
    print("Se terminaron tus intentos. El número era ",a)