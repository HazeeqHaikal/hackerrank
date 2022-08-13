truth = True
arr = []

while truth:
    askNumber = str(input())
    if(int(askNumber) == -7):
        truth = False
    else:
        arr.append(askNumber)
sum = []

for x in arr:
    sum.append(int(x, 8))

sumTotal = 0

for x in sum:
    sumTotal += x

print(oct(sumTotal)[2:])
    