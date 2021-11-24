import math
print("Introduza o valores no eixo x e y dos dois pontos no mapa cartesiano.")
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
d=((x2-x1)**2+(y2-y1)**2)
print(math.sqrt(d))