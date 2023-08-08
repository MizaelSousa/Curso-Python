#ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela!!!

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))

print('So tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta em maiusculas?', a.isupper())
print('Esta em minusculas?', a.islower())
print('Esta captalizada?', a.istitle())
