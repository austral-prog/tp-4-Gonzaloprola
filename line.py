def line():
    print("TO DO")
    
    import math

A = float(input("Ingrese el coeficiente A: "))
B = float(input("Ingrese el coeficiente B: "))
x1 = float(input("Ingrese el coeficiente X1: "))
x2 = float(input("Ingrese el coeficiente X2: "))

print(f"El coeficiente A de su ecuación de la recta es:{A}")
print(f"El coeficiente B de su ecuación de la recta es: {B}")
print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")

print(f"y = {A}x + {B}")

Y1 = A * x1 + B
Y2 = A * x2 + B

print("Para la siguiente ecuación:")
print(f"/tP1 ({x1} ; {Y1}) ")
print(f"/tP2 ({x2} ; {Y2}) ")


Distancia = math.sqrt((x2 - x1)**2 + (Y1 - Y2)**2)

print(f"La distancia entre ellos es:{Distancia}")

 
