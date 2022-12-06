f = open('C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q5\\input.txt', "r")
data = f.read()

data = data.split("\n\n")
order = data[1]
data = data[0].split('\n')
temp = data[-1].split()
all = {}
for i in range(len(temp)):
    printData = []
    for j in range(len(data)-1):
        if (data[j][i*4:(i+1)*4][0:-1][1]).isalpha():

            printData.append(data[j][i*4:(i+1)*4][0:-1][1])

    all[temp[i]] = printData
print(all)

order = order.split('\n')
for i in range(len(order)):
    read = order[i]

    read1 = [int(read[read.find("move")+4:read.find(" from")].strip()), read[read.find(
        "m ")+2:read.find("m ")+3], read[read.find("o ")+2:read.find("o ")+3]]
    order[i] = read1

# for i in range(len(order)):
#     for j in range(order[i][0]):
#         moveFrom = all[order[i][1]]

#         if len(moveFrom) > 0:
#             delive = moveFrom.pop(0)

#             moveTo = all[order[i][2]]
#             moveTo.insert(0, delive)
#             all[order[i][2]] = moveTo
#             all[order[i][1]] = moveFrom
# allKeys = list(all.keys())
# res = ""

# for i in range(len(allKeys)):
#     res += all[allKeys[i]][0] if len(all[allKeys[i]])>0 else ""
# print(all)
# print(res)


# part 2


for i in range(len(order)):
    moveFrom = all[order[i][1]]
   
    delive = moveFrom[0:min(len(moveFrom), order[i][0])]
    moveTo = all[order[i][2]]
    moveTo = delive+moveTo
    
    all[order[i][2]] = moveTo
    all[order[i][1]] = all[order[i][1]][order[i][0]:]


allKeys = list(all.keys())
res = ""

for i in range(len(allKeys)):
    res += all[allKeys[i]][0] if len(all[allKeys[i]]) > 0 else ""
print(all)
print(res)
