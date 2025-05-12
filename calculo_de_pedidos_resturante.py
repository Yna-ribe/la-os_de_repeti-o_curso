print(' Digite quais pratos você deseja pedir: ')
quantidade_entrada=int(input('digite quantas da entrada: '))
quantidade_prato_principal=int(input('digite quantos da prato principal: '))
quantidade_sobremesa=int(input('digite quantas da sobremesa: '))

entrada=20.00
prato_principal=50.00
sobremesa=15.00

total=(entrada*quantidade_entrada)+(prato_principal*quantidade_prato_principal)+(sobremesa*quantidade_sobremesa)

if (total >130):
  resultado = total - (total*0.10)
  print(f'Parabéns você ganho um desconto de 10%, o valor total do seu pedido é {resultado}')

else:
  print(f'O valor total do seu pedido é {total}')