#Desafio010 - Crie um programa que leia a largura e a altura da parede em metros, 
#calcule sua área e a quantidade de tinta necessaria para pinta-la, 
#sabendo que cada litro de tinta, pinta uma are de 2m².

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
qtd_tinta = area / 2

print('Area da parede: {}m²'
      '\nNecessário {:.2f} litros de tinta para pinta-la'.format(area, qtd_tinta))
