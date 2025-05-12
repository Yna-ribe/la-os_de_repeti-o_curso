print('Bem vindo a calculadora de média')
numeros=[]
for i in range(3):
    numero= int(input('digite sua nota: '))
    print(numero)
    numeros.append(numero)
soma=sum(numeros)
media=(soma)/3
print('media do aluno é:',media)