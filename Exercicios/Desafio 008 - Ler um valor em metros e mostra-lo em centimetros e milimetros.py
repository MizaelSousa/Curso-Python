#Desafio008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valor_metro = float(input('Digite o valor em metros: '))

centimetros = valor_metro * 100
milimetros = valor_metro * 1000

print('{:1} metros equivalem a:'
      '\n{:1} centimentros'
      '\n{:1} milimetros'.format(valor_metro, centimetros, milimetros))
