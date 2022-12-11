import math
f = open(
    'C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q9\\input.txt', "r")
data = f.read()
data = data.split("\n")

du = 0
lr = 0
for i in data:
    direc, step = i.split()
    if direc == "U" or direc == "D":
        du = max(du, int(step))
    else:
        lr = max(lr, int(step))
print(du, lr)


init = []
for i in range(du):
    init.append([0]*lr)
init[-1][0] = 1


def lenght(head, tail):
    x1, y1 = head
    x2, y2 = tail
    return (math.sqrt((x1-x2)**2 + (y1-y2)**2))


def move(d, point):
    if d == "R":
        point[1] += 1
    elif d == "L":
        point[1] -= 1
    elif d == "U":
        point[0] -= 1
    else:
        point[0] += 1


def bestMove(head, tail):
    if lenght(head, [tail[0], tail[1]]) <2:
        return tail

    if lenght(head, [tail[0], tail[1]+1]) <= 1:
        return [tail[0], tail[1]+1]
    elif lenght(head, [tail[0], tail[1]-1]) <= 1:
        return [tail[0], tail[1]-1]
    elif lenght(head, [tail[0]-1, tail[1]]) <= 1:
        return [tail[0]-1, tail[1]]
    elif lenght(head, [tail[0]+1, tail[1]]) <= 1:
        return [tail[0]+1, tail[1]]

    elif lenght(head, [tail[0]+1, tail[1]-1]) <= 1:
        return [tail[0]+1, tail[1]-1]
    elif lenght(head, [tail[0]+1, tail[1]+1]) <= 1:
        return [tail[0]+1, tail[1]+1]
    elif lenght(head, [tail[0]-1, tail[1]+1]) <= 1:
        return [tail[0]-1, tail[1]+1]
    elif lenght(head, [tail[0]-1, tail[1]-1]) <= 1:
        return [tail[0]-1, tail[1]-1]

# Trick


def follow(tail, head):
    if all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)]):
        return tail
    (tail_x, tail_y), (head_x, head_y) = tail, head
    if tail_x == head_x:
        tail[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        tail[0] += int(tail_x < head_x) * 2 - 1
    else:
        tail[0] += int(tail_x < head_x) * 2 - 1
        tail[1] += int(tail_y < head_y) * 2 - 1
    return tail


def printAll(head, tail):
    init = []

    for i in range(du):
        init.append(["."]*6)
    init[head[0]][head[1]] = "H"
    init[tail[0]][tail[1]] = "T"
    s = ""
    for i in range(len(init)):
        for j in range(len(init[i])):
            s += init[i][j]
        s += "\n"
    print(s)


head, tail = [0, 0], [0, 0]
tail1 = tail.copy()
tail2 = tail.copy()
tail3 = tail.copy()
tail4 = tail.copy()
tail5 = tail.copy()
tail6 = tail.copy()
tail7 = tail.copy()
tail8 = tail.copy()
tail9 = tail.copy()
visited_one = {tuple(head)}
visited_2 = {tuple(head)}
for i in data:
    direction, step = i.split()
    for j in range(int(step)):
        move(direction, head)
        if lenght(head, tail) >= 2:
            currBest = bestMove(head, tail)
            tail = currBest
            visited_one.add(tuple(tail))
        tail1 = follow(tail1, head)
        tail2 = follow(tail2, tail1)
        tail3 = follow(tail3, tail2)
        tail4 = follow(tail4, tail3)
        tail5 = follow(tail5, tail4)
        tail6 = follow(tail6, tail5)
        tail7 = follow(tail7, tail6)
        tail8 = follow(tail8, tail7)
        tail9 = follow(tail9, tail8)
        visited_2.add(tuple(tail9))


