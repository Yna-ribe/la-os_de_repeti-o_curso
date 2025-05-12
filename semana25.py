assentos= [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
  ]
def reservar():
    coluna = int(input('digite a fileira que deseja reservar 0 - 4 '))
    assento = int(input('digite o assento que deseja reservar 0 - 7 '))
    assentos[coluna][assento] = 1
def cancelar():
    coluna = int(input('digite a fileira que deseja cancelar 0 - 4 '))
    assento = int(input('digite o assento que deseja cancelar 0 - 7 '))
    assentos[coluna][assento] = 0
def exibir():
  for i in assentos:
    print(i)

reservar()
cancelar()
exibir()