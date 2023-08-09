#Desafio014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

graus_c = float(input('Informe a temperatura em °C: '))
graus_f = ((9 * graus_c) / 5) + 32
print('A temeperatura de {} °C corresponde a {} °F.'.format(graus_c, graus_f))
