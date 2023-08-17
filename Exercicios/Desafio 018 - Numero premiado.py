#Desafio018 - Escreva um programa que faça o computador pensar em um numero entre 0 e 5 e peça para o usuario tentar descobrir  qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu!

import random

numero_escolha = int(input("Digite um numero entre 1 e 5 e tente descobrir o numero vencedor:"))

numero = random.randint(1,5)

if numero_escolha <= 0 or numero_escolha >=6:
    print("Você digitou um numero que não pertece ao jogo!!!")
elif numero_escolha == numero:
    print("Parabens, você acertou o numero premiado!!!")
else:
    print("Desculpe, você não acertou o numero premiado. Tente outra vez!!!")
