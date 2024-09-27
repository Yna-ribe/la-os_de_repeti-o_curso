nota1=float(input('digite a primeira nota: '))
nota2=float(input('digite a segunda nota: '))

while(nota1<0 or nota1 > 10 or nota2 <0 or nota2>10):
    print("Nota inválida")
    nota1=float(input('digite a primeira nota: '))
    nota2=float(input('digite a segunda nota: '))
resultado=(nota1+nota2)/2 
print('sua média é:', resultado)