f = open(
    'C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q10\\input.txt', "r")
data = f.read()
data = data.split("\n")

# stage = 0
# value = 1
# total = 0
# for i in data:
#     loop = 2 if "addx" in i else 1
#     for j in range(loop):
#         stage += 1
#         if (stage-20) % 40 == 0:
#             total += (stage*value)
#     if loop == 2:
#         value += int(i.split()[1])


# part 2
stage = 0
value = 1
sprite = [".", ".", "."]
positon = [0, 1, 2]
while len(sprite) < 40:
    sprite.append(".")
print(len(sprite))
total40 = []
stringTest = []
for i in data:
    loop = 2 if "addx" in i else 1
    for j in range(loop):
        if stage == 40:
            stage = 0
        if len(total40) == 40:
            print(total40)
            stringTest.append(total40)
            total40 = []
        
        print(stage, positon)
        if stage in positon:
            total40.append("#")
        else:
            total40.append(".")
        print(total40)
        stage += 1

    if loop == 2:
        tooMove = int(i.split()[1])
        positon[0] += tooMove
        positon[1] += tooMove
        positon[2] += tooMove
stringTest.append(total40)
  
for i in range(len(stringTest)):
    prints = ""
    for j in range(len(stringTest[0])):
        prints += stringTest[i][j]
    print(prints)
print(stage)