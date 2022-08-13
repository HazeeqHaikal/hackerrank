subjectAmount = int(input())

arr = []

for x in range(0, subjectAmount):
    arr.append(str(input()))

arr2 = {}

for x in arr:
    splitComma = x.split(',')
    c = ""
    for a in splitComma:
        c = a.strip()
    arr2.update({splitComma[0]:c})
    
for key, value in arr2.items():
    calculate = eval(value) * 100
    arr2.update({key:calculate})
    
sorted_x = dict(sorted(arr2.items(), key=lambda kv: kv[1], reverse=True))
res = list(sorted_x.keys())[0]

print(res)