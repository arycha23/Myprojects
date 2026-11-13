dict = {0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"}

i = (input("Enter number: "))
x = [0]*len(i)
last = len(i) -1
i = int(i)

while (i > 0):
    x[last] = (i % 10)
    last =  last -1
    i = int(i/10)


for a in range(0, len(x)):
    print(dict[x[a]])