numero = int(input('Digite um número: '))
numeros = []
for i in range(10):
  numeros.append(numero)
  print(numeros)
print(f"N[{i}] = {numeros[i]}")
numero = numero * 2
print(f"N[{i}] = {numeros[i]}")