n = int(input("enter number to delete : "))
arr1 = [10,20,30,40,50,60,70,80,90]
arr2 = [0] * len(arr1)
i = 0
for num in arr1:
    if(num != n):
        arr2[i] = num
        i = i+1
print(arr2)

for num in arr1:
    print(arr1)