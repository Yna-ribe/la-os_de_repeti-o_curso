m=[[10,20,4,54],
  [25,9,14,18],
  [3,42,5,4]]

maior_valor=[]

for linha in range(len(m)):
  maior_valor.append(max(m[linha]))
print(max(maior_valor))