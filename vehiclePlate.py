askForNumber = int(input().strip())
arr = []

for x in range(0, askForNumber):
    plate = str(input())
    arr.append(plate)
    
arr2 = {}

for x in arr:
    sum = 0
    for a in x:
        try:
            sum += int(a)
        except:
            pass
    keyUpdate = {x:sum}
    arr2.update(keyUpdate)

for key, value in arr2.items():
    if value % 2 != 0:
        print(key)
    else:
        print(value)


        

