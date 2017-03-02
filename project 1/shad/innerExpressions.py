ret = [(x,y) for x in (1,3,5)
       for y in (4,3,5)
       if x!=y]
print (ret)

matrix = [(1, 2, 3, 5),
          (2, 4, 8, 10),
          (4, 6, 8, 15)]
transposition = [[row[i] for row in matrix]
                 for i in range(len(matrix[0]))]
print(transposition)