file = open("1/1.txt", "r")
lines = file.readlines()

maxCal = [0, 0, 0]
temp = 0
for l in lines:
    l = l.strip()
    if len(l) > 0:
        temp = temp + int(l)
    else:
        for i in range(0, len(maxCal)):
            if maxCal[i] < temp:
                maxCal.insert(i, temp)
                maxCal.pop()
                break
        temp = 0

val = 0
for mc in maxCal:
    val = val + mc
print(val)
# Don't like this solution but it will do for now