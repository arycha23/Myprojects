m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for x in range(0,len(m)):
    for y in range(0,len(m)):
        if(m[x][y] % 2 == 1):
            m[x][y] = m[x][y] * m[x][y]
print(m)