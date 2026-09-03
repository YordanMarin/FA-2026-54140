import math

num = float(input("Ingrese un número decimal: "))

r2 = math.sqrt(num)
redo = round(num)
r3 = math.pow(num,3) #num**3
rcu = num**(1/3)

print("\nRaíz cuadrada: ", r2)
print("Redondeado a entero: ",redo)
print("Al cubo: ", r3)
print("Raíz cubica: ",rcu)