file = open("3/3.txt", "r")
lines = file.readlines()
sum = 0



for x in lines:
    h = len(x.strip())/2
    l = x[:int(h)]
    r = x[int(h):]
    for y in range(len(l)):
        if l[y] in r:
            print("letter:" , l[y])
            print(l, r)
            val_char = ord(l[y])
            if val_char <= 90:
                sum += val_char-38
            else:
                sum += val_char-96
            break
print(sum)
print(ord('r')-96)
print(ord('A')-38)