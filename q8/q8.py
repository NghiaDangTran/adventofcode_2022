f = open(
    'C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q8\\input.txt', "r")
data = f.read()
data = data.split("\n")
total = len(data)*2+len(data[0])*2-4
for i in range(len(data)):
    data[i] = list(data[i])

table = []
table.append([True]*len(data[0]))
for i in range(1, len(data)-1, 1):
    table.append([True]+[False]*(len(data[0])-2)+[True])
table.append([True]*len(data[0]))


def newLoop(start, stop, step, i, j, direction):
    curr = data[i][j]
    # print(curr," baxl")
    show = ""
    for k in range(start, stop, step):
        if direction == 1:
            show += str(data[i][k]) + " "
            if data[i][k] >= curr:
                return False
        elif direction == 2:
            show += str(data[k][j])+" "
            if data[k][j] >= curr:
                return False

    # print(show)
    return True


def Pointcal(start, stop, step, i, j, direction):
    curr = data[i][j]
    point = 0
    show = ""
    for k in range(start, stop, step):
        if direction == 1:
            show += str(data[i][k]) + " "
            if data[i][k] < curr:
                point += 1
            else:
                point += 1
                break
        elif direction == 2:
            show += str(data[k][j])+" "
            if data[k][j] < curr:
                point += 1
            else:
                point += 1
                break

    return point


print(data)

for i in range(1, len(data)-1, 1):
    for j in range(1, len(data[0])-1, 1):
        # print(newLoop(i+1, len(data), 1, i, j, 2))
        if newLoop(j-1, -1, -1, i, j, 1) or newLoop(j+1, len(data[0]), 1, i, j, 1) or newLoop(i-1, -1, -1, i, j, 2) or newLoop(i+1, len(data), 1, i, j, 2):
            total += 1


# part2
currMax = 0
for i in range(1, len(data)-1, 1):
    for j in range(1, len(data[0])-1, 1):
        # print(newLoop(i+1, len(data), 1, i, j, 2))
        currMax = max(currMax, Pointcal(j-1, -1, -1, i, j, 1)*Pointcal(j+1, len(
            data[0]), 1, i, j, 1)*Pointcal(i-1, -1, -1, i, j, 2)*Pointcal(i+1, len(data), 1, i, j, 2))
        # if newLoop(j-1, -1, -1, i, j, 1) or newLoop(j+1, len(data[0]), 1, i, j, 1) or newLoop(i-1, -1, -1, i, j, 2) or newLoop(i+1, len(data), 1, i, j, 2):
        #     total += 1


print(currMax)
