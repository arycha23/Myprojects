a = ["(","(","[","]",")",")"]
r = len(a) - 1
l = 0

while (r > l):

    if (a[r] == ')' or a[r]==']') and  (a[l]=='(' or a[l]=='['):
        print("valid")
    else:
        print("invalid")
        break

    r = len(a) - 1
    l = len(a) + 1

