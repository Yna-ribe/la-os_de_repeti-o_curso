print('Bem vindo(a) ao programa de funções com listas!')
quantidade_notas=int(input('digite a quantidade de notas: '))


notas=[]
i=0
for i in range (1,quantidade_notas+1):
    nota=int(input('digite a nota: '))
    notas.append(nota)
print('A lista digitada é: ', notas)
for i in range(len(notas)):
  soma=sum(notas)
  media=soma/quantidade_notas
print('A média da lista de notas é: ', media)