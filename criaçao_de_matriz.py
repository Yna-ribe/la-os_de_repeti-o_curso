adicionar=int(input('Digite 1 para adicionar os vetores: '))
vezes=int(input('digite o numero de vetores que deseja criar: '))

numeros = []

while (adicionar == 1): 
  for i in range (vezes):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
  print(numeros)
  break
oque_fazer=int(input('2)deseja excluir, 3)editar ou 0 para finalizar: '))
if (oque_fazer==2):
  print(numeros)
  apagar=int(input('qual você deseja apagar {}: '))
  numeros.remove(numeros[apagar])
  print(numeros)
elif (oque_fazer==3):
  print(numeros)
  editar=int(input('qual deseja editar{}: '))
  novo_numero=int(input(f'digite o novo valor para a posição {editar}: '))
  numeros.insert(editar,novo_numero)
  print(numeros)
elif (oque_fazer==0):
  print('saindo')