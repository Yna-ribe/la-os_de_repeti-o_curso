idade=int(input('digite sua idade: '))
genero=input('indique qual gênero de filme você prefere: Comedia, Ação ou Drama: ')

while (idade >= 18):
  if (genero == 'Comedia'):
     print('Você deve assistir: \n Festa das salsichas,\n American PIE,\n Mais um besteirou americano \n e muito mais...')
  elif (genero == 'Ação'):
     print('Você deve assistir: \n Velozes e Furiosos, \n Vingadores, \n Missão Impossível, \n Mulher Maravilha \n e muito mais...')
  elif (genero == 'Drama'):
     print('Você deve assistir: \n Um namorado para minha esposa, \n A culpa é das estrelas, \n O dia do meu primeiro casamento \n e muito mais...')
  else:
     print('Gênero inválido')
  break

while (idade < 18):
  if (genero == 'Comedia'):
    print('Você deve assistir: \n Escola de rock,\n Turma do Barulho,\n Zootopia \n e muito mais...')
  elif (genero == 'Ação'):
    print('Você deve assistir: \n Fuga das galinhas, \n Batutinhas, \n Harry Potter e a pedra filosofal, \n e muito mais...')
  elif (genero == 'Drama'):
    print('Você deve assistir: \n Frozen, \n Divertidamente, \n Extraordinario \n e muito mais...')
  else:
    print('Gênero inválido')
  break