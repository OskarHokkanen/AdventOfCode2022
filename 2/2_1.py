#A Rock + 1
#B Paper + 2
#C Scissors + 3

#Win 6
#Draw 3
#Loss 0

def calc_extra_score(type):
    if type == "X":
        return 1
    if type == "Y":
        return 2
    if type == "Z":
        return 3

def calc_result(myMove, opponentsMove):
    if ord(opponentsMove) == ord(myMove)-23:
        return 3
    if myMove == "X":
        if opponentsMove == "B":
            return 0
        else:
            return 6
    if myMove == "Y":
        if opponentsMove == "C":
            return 0
        else:
            return 6
    if myMove == "Z":
        if opponentsMove == "A":
            return 0
        else:
            return 6


file = open("2/2.txt", "r")
lines = file.readlines()

sum = 0
for l in lines:
    l = l.strip()
    sum = sum + calc_result(l[2], l[0])
    sum = sum + calc_extra_score(l[2])

print(sum)
print(ord("X") - 23, ord("A"))
print(ord("Y"), ord("B"))
print(ord("Z"), ord("C"))

# (S)67/(P)66 (P)66/(R)65 1 == WIN