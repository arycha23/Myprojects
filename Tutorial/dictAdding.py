x = {"apple":2, "banana":3}
y = {"apple":3, "grape":1, "orange":7}

for key in y:
    if (key in x):
        x[key]= x[key]+ y[key]
    else:
        x[key]= y[key]
print(x)