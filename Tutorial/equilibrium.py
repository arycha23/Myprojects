a = [1, 5, 3, 2, 1, 3, 7]

l = 0
r = len(a) - 1
l_sum = a[l]
r_sum = a[r]

while (l < r):
    if (l_sum < r_sum):
        l = l + 1
        l_sum = l_sum + a[l]
    elif (l_sum > r_sum):
        r = r - 1
        r_sum = r_sum + a[r]
    elif(l_sum == r_sum):
        print(f"left index {l}, right index {r}, value = {l_sum}")
        break
else:
    print("no equilibrium found")
