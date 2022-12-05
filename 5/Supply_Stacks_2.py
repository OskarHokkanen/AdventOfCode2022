import re
#               STACKS
#####################################
#                         [Z] [W] [Z]
#         [D] [M]         [L] [P] [G]
#     [S] [N] [R]         [S] [F] [N]
#     [N] [J] [W]     [J] [F] [D] [F]
# [N] [H] [G] [J]     [H] [Q] [H] [P]
# [V] [J] [T] [F] [H] [Z] [R] [L] [M]
# [C] [M] [C] [D] [F] [T] [P] [S] [S]
# [S] [Z] [M] [T] [P] [C] [D] [C] [D]
#  1   2   3   4   5   6   7   8   9 
#####################################
file = open("5/5.txt", "r")
lines = file.readlines()
ans = 0

stacks = [
    ['N', 'V', 'C', 'S'],
    ['S', 'N', 'H', 'J', 'M', 'Z'],
    ['D', 'N', 'J', 'G', 'T', 'C', 'M'],
    ['M', 'R', 'W', 'J', 'F', 'D', 'T'],
    ['H', 'F', 'P'],
    ['J', 'H', 'Z', 'T', 'C'],
    ['Z', 'L', 'S', 'F', 'Q', 'R', 'P', 'D'],
    ['W', 'P', 'F', 'D', 'H', 'L', 'S', 'C'],
    ['Z', 'G', 'N', 'F', 'P', 'M', 'S', 'D']
]

for line in lines:
    line = line.strip()
    move = re.findall('\d+', line)
    n = int(move[0])
    frm = int(move[1])-1
    to = int(move[2])-1
    items = stacks[frm][0:n]
    stacks[frm] = stacks[frm][n:]
    items.extend(stacks[to])
    stacks[to] = items
    
    
ans = ""        
for y in stacks:
    ans += y[0]
print(ans)
#n, frm, to