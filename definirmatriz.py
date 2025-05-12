m=[[10,20,4,54],
  [15, 3, 4, 54],
   [90, 9, 14, 18],
   [30, 2, 5, 4]]

pares=int(0)
for linha in range(len(m)):
  for i in range(len(m[linha])):
    if(m[linha][i]%2==0):
      pares=pares+1