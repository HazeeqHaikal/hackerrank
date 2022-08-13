arr = []
arr2 = []
arr3 = []

arr.append(list(map(int, input().rstrip().split())))

for x in arr:
    for a in x:
        arr3.append(a)

arr = arr3
# print(arr)

truth = True
count = 1

askForNumber = int(input().strip())
# print(askForNumber)
# askForNumber = 5

for x in range(0, askForNumber):
    equation = arr[0] + (count + len(arr) - 1) * (arr[1] - arr[0])
    arr2.append(equation)
    count += 1

for x in arr2:
    arr.append(x)

print(' '.join(str(x) for x in arr))
# print(" ".join(arr))

