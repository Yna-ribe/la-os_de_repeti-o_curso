print('digite 1 para graus celcius')
print( 'digite 2 para graus fahrenheit')
print ( 'digite 0 para sair')
numero=int(input('digite um numero para verificar ou 0 para sair: '))

while(numero!=0):
    if(numero == 1):
        valor=int(input('digite o valor em graus celcius:' ))
        resultado=(valor * 9/5) + 32
        print('o valor em fahrenheit é:', resultado)
    elif(numero == 2):
        valor=int(input('digite o valor em graus fahrenheit:' ))
        resultado=(valor - 32) * 5/9
        print('o valor em celcius é:', resultado)
    else:
        print('saindo')
    numero=int(input('digite um numero para verificar ou 0 para sair: '))