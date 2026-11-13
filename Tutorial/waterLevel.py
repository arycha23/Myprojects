a = [2,8,5,9,2,6]
max_water = 0
r = 0
l = len(a)- 1

while(r < l):
    width = l - r
    height = min(a[r], a[l])
    area = height * width

    if (a[r] > a[l]):
        l = l - 1
    else:
        r = r + 1

    if(area > max_water):
        max_water = area

print(max_water)