import math
diametro=float(input("ingrese el diametro del circulo"))

radio=diametro/2

perimetro=math.pi * diametro

area = math.pi * (radio ** 2)

print(f"El radio del círculo es: {radio}")
print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")
