m = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
m2 = [[1, 2, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

for i in range(len(m)):
   while len(m[i]) == len(m):
      print('é matriz identidade')
   if len(m[i]) != len(m):
      print('não é matriz identidade')