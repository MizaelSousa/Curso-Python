#Desafio013 - Crie um algoritmo que calcule o reajuste salarial de um funcionario!

nome = input('Digite o nome do funcionario: ')
salario = float(input('Digite o salario do funcionario: '))
porcentagem_aumento = int(input('Digite a porcentagem do aumento: '))

aumento = salario * (porcentagem_aumento / 100)
novo_salario = salario + aumento
#novo_salario = salario + (salario * porcentagem_aumento / 100)

print('-'*20)
print('Funcionario: {}'
      '\nSalario atual: {}'
      '\nPorcentagem de aumento: {}'
      '\nValor do aumento: {:.2f}'
      '\nNovo salario: {}'
      .format(nome, salario, porcentagem_aumento, aumento, novo_salario))
