from collections import Counter
f = open('C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q3\\input.txt', "r")
data = f.read()

data = data.split("\n")


def val(a):
    if a.islower():

        return ord(a)-ord("a")+1
    return ord(a)-ord("A")+27

# part1
# res = 0

# for i in range(len(data)):
#     a = Counter(data[i][0:int(len(data[i])/2)])
#     b = Counter(data[i][int(len(data[i])/2):])
#     check = dict(a & b)
#     # intersection of a and b
#     temp = list(check.keys())
#     for j in range(len(temp)):
#         if not temp[j].isnumeric():
#             res += val(temp[j])


# print(res)

# part 2
res = 0
for i in range(0, len(data), 3):
    print(i, i+1, i+2)
    a = Counter(data[i])
    b = Counter(data[i+1])
    c = Counter(data[i+2])
    check = dict(a & b & c)
    # intersection of a and b
    temp = list(check.keys())
    for j in range(len(temp)):
        if not temp[j].isnumeric():
            res += val(temp[j])
print(res)
