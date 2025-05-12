  dados= [
    [22,25,28,32],
    [20,23,26,30],
    [18,22,25,29]
  ]
  dados_reeorganizados=[]
  dados_reeorganizados1=[]
  for vetores in range(4):
      meses=[]
      for linhas in range(3):
          meses.append(dados[linhas][vetores])
      dados_reeorganizados.append(meses)
  for vetores in range(3):
      cidades=[]
      for linhas in range(4):
          cidades.append(dados[vetores][linhas])
      dados_reeorganizados1.append(cidades)
  print("meses")
  for linha in dados_reeorganizados:
      print(linha)
  print("cidades")
  for linha2 in dados_reeorganizados1:
      print(linha2)
