#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o cumprimento da hipotenusa.
#h = √(a² + b²)
import math

x = float(input('Digite o valor do eixo x: '))
y = float(input('Digite o valor do eixo y: '))
h = math.hypot(x, y)

#h = (x ** 2 + y ** 2) ** (1/2)

#calc = (x * x) + (y * y)
#h = calc ** (1/2)

print('A hipotenusa é igual a: {:.2f}'.format(h))
