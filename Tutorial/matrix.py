m = [[1, 8, 9],
    [2, 7, 3],
    [8, 1, 6]]


n=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]

for r in range(0, len(m)):
    for c in range(0, len(m)):
        n[r][c] = m[r][c]
        n[r][len(m)] = n[r][c] + n[r][len(m)]
        n[len(m)][c] = n[r][c] + n[len(m)][c]
print(n)