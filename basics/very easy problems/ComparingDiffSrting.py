#int,srt, float,character
##int& flaot = same #
## str and chara = same character
### compare if things are same or not
import math
from math import *

iNumber = int(input("Enter number: "))
fNumber = float(input("Enter float number: "))


if (iNumber == fNumber):
    print("equal")
else:
    print("not equal")

print(iNumber / fNumber)
print(ceil(iNumber / fNumber))

print(fNumber / iNumber)
print(ceil(fNumber / iNumber))