#Desafio016 - Crie um programa que leia um numero Real qualquer e mostre na tela a sua porção inteira.
import math

numero = float(input('Digite um numero real: '))

print('O numero {} tem a parte inteira {}'.format(numero, math.trunc(numero)))
