x = ['a','b','c','a','d','b']
dict = {}
for i in range (0,len(x)):
    v = 0
    if (x[i] in dict):
        v = dict[x[i]]
    dict[x[i]] = v + 1

print(dict)



