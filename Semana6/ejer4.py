password = "hola123"
intentos = 3

while intentos > 0:
    contra = input(f"Intento {intentos}. Ingrese la contraseña: ")

    if password == contra:
        print("Acceso concebido.\n")
        break
    else:
        print("Contraseña incorrecta.\n")
        intentos-=1

if intentos ==0:
    print("Se agotaron los intentos. Sistema bloqueado!")