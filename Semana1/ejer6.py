seg = int(input("Ingresar los segundos: "))

horas = seg // 3600
minu = (seg % 3600) // 60
res = seg % 60

print(f"{horas} : {minu} : {res}")