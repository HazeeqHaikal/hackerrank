import datetime

askTime = str(input())
timeSplit = askTime.split(":")

askSecond = int(input())

a = datetime.datetime(100, 1, 1, int(timeSplit[0]), int(timeSplit[1]), int(timeSplit[2]))
b = a + datetime.timedelta(0, askSecond)

print(b.strftime("%H:%M:%S"))

