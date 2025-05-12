print('Bem vindo(a) ao programa de organização de números!')

numeros=[]
for i in range (5):
    n=int(input('digite um número: '))
    numeros.append(n)
soma=sum(numeros)
print(f'soma dos numero é: {soma}')