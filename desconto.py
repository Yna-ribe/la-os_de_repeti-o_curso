print("desconto")
itens=float(input('digite a quantidade de itens: '))
valor=float(input('digite o valor: '))
if(itens >=6 and itens <=10):
   valor=valor/100*90
   print(f'valor a pagar{valor}')
elif(itens >10 ):
  valor=valor/100*80
  print(f'valor a pagar{valor}')
else:
  print(f'sem desconto {valor} reais')