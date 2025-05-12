n=int(input('digite um numero fatorial: '))
def fatorial(n):
  resultado=1
  for i in range(1,n+1):
    resultado=resultado*i
  return resultado
resultado=fatorial(n)
print(f'O resultado da fatoração é: {resultado}')