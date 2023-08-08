#Desafio005 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e o seu antecessor.

n = int(input('Digite um numero: '))

sucessor = n + 1
antecessor = n - 1

print('O numero digitado foi: {}'
      '\nO seu sucessor é: {}'
      '\nO seu antecessor é: {}'
      .format(n, sucessor, antecessor))
