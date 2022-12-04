file = open("4/4.txt", "r")
lines = file.readlines()
ans = 0

for line in lines:
    pair = line.strip().split(",")
    l_p = pair[0].split("-")
    r_p = pair[1].split("-")
    if (int(l_p[0]) >= int(r_p[0]) and int(l_p[1]) <= int(r_p[1])) or (int(r_p[0]) >= int(l_p[0]) and int(r_p[1]) <= int(l_p[1])):
        print(pair, "True")
        ans += 1
    else: 
        print(pair, "False")
print (ans)
