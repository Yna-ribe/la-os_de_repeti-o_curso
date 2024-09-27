numero = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))
soma = 0
while (numero < numero2):
  numero = numero + 1
  if (numero % 2 != 0):
    soma = soma + numero
print('a soma dos impares é: ', soma)