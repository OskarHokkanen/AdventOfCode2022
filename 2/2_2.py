#A Rock + 1
#B Paper + 2
#C Scissors + 3

#Win 6
#Draw 3
#Loss 0
def get_move(myMove, opMove):
    if myMove == "Z":
        if opMove == "A":
            return "Y"
        if opMove == "B":
            return "Z"
        if opMove == "C":
            return "X"
    if myMove == "X":
        if opMove == "A":
            return "Z"
        if opMove == "B":
            return "X"
        if opMove == "C":
            return "Y"
    if myMove == "Y":
        return chr(ord(opMove) + 23)


def calc_extra_score(type):
    if type == "X":
        return 1
    if type == "Y":
        return 2
    if type == "Z":
        return 3

# X WIN
# Y DRAW
# Z LOSE 
def calc_result(myMove, opponentsMove):
    mm = get_move(myMove, opponentsMove)
    extra = calc_extra_score(mm)
    if ord(opponentsMove) == ord(mm)-23:
        return 3 + extra
    if mm == "X":
        if opponentsMove == "B":
            return 0 + extra
        else:
            return 6 + extra
    if mm == "Y":
        if opponentsMove == "C":
            return 0 + extra
        else:
            return 6 + extra
    if mm == "Z":
        if opponentsMove == "A":
            return 0 + extra
        else:
            return 6 + extra


file = open("2/2.txt", "r")
lines = file.readlines()

sum = 0
for l in lines:
    l = l.strip()
    sum = sum + calc_result(l[2], l[0])

print(sum)

# This one looks really bad. However i just wanted to finish it.
