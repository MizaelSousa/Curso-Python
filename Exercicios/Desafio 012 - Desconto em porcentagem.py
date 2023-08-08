#Desafio012 - Crie um programa que leia o preço de um produto e ostre seu novo preço com 5% de desconto

valor_do_produto = float(input('Digite o valor do produto: '))
porcentagem_de_desconto = float(input('Digite a porcentagem de desconto: '))

desconto = valor_do_produto * (porcentagem_de_desconto / 100)
novo_valor = valor_do_produto - desconto

print('-'*15)
print('Valor do produto: {}'
      '\nPorcentagem de desconto: {}'
      '\nValor do desconto: {}'
      '\nValor com desconto: {}'.format(valor_do_produto, porcentagem_de_desconto, desconto, novo_valor))
