#Desafio006 - Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero: '))

dobro = n * 2
triplo = n * 3
raiz_quadrada = n ** (1/2)

print('O valor digitado foi: {}'
      '\nO dobro é: {}'
      '\nO triplo é: {}'
      '\nA raiz quadrada é: {:1f}'.format(n, dobro, triplo, raiz_quadrada))
