#Desafio007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

nome = input('Digite o nome do aluno(a): ')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

print('A média final de {} foi: {}'.format(nome, media))

if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')
