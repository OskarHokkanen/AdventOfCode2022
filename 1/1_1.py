file = open("1/1.txt", "r")
lines = file.readlines()

maxCal = 0
temp = 0
for l in lines:
    l = l.strip()
    if len(l) > 0:
        temp = temp + int(l)
    else:
        if maxCal < temp:
            maxCal = temp
        temp = 0
print(maxCal)
