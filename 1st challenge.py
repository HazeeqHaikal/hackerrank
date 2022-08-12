num = [4, 73, 67, 38, 33]

for i in num:
    if (i % 5 >= 3 and i >= 38):
        while i % 5 != 0 :
            i += 1
        print("Finished Rounding: ", i)
    else:
        print("No Rounding: ", i)
