file = open("3/3.txt", "r")
lines = file.readlines()
sum = 0


for x in range(0, len(lines), 3):
    one = lines[x].strip()
    two = lines[x+1].strip()
    three = lines[x+2].strip()

    group = [one, two, three]
    group.sort(reverse=False,key=len)

    for y in range(len(group[0])):
        letter = group[0][y]
        if letter in group[1] and letter in group[2]:
            val_char = ord(letter)
            if val_char <= 90:
                sum += val_char-38
            else:
                sum += val_char-96
            break
print(sum)
print(ord('p')-96)
print(ord('A')-38)