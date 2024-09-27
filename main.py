numeros_impares=0
numeros_pares=0
numeros_negativos=0
numeros_postivos=0
for i in range(5):
  numero= int(input('digite um numero'))
  print(numero)
  if (numero>0):
    numeros_postivos=numeros_postivos+1
  else:
    numeros_negativos=numeros_negativos+1
  if(numero%2==0):
    numeros_pares=numeros_pares+1
  else:
    numeros_impares=numeros_impares+1
print('numeros pares',numeros_pares)
print('numeros impares',numeros_impares)
print('numeros positivos',numeros_postivos)
print('numeros negativos',numeros_negativos)