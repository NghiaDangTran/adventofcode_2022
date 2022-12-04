f = open('C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q4\\input.txt', "r")
data = f.read()

data = data.split("\n")
res = 0
# part1
# for i in data:
#     split1 = i.split(",")
#     l = split1[0].split("-")
#     l_begin, l_end = int(l[0]), int(l[1])
#     r = split1[1].split("-")
#     r_begin, r_end = int(r[0]), int(r[1])
#     if l_begin <= r_begin and l_end >= r_end:
#         print(l_begin,l_end,r_begin,r_end)
#         res += 1
#     elif l_begin >= r_begin and l_end <= r_end:
#         print(l_begin,l_end,r_begin,r_end)

#         res += 1
# print(res)

# part2
for i in data:
    split1 = i.split(",")
    l = split1[0].split("-")
    l_begin, l_end = int(l[0]), int(l[1])
    r = split1[1].split("-")
    r_begin, r_end = int(r[0]), int(r[1])
    a=set(range(l_begin,l_end+1))
    b=range(r_begin,r_end+1)
    
    if len(a.intersection(b))>0:
        res+=1
print(res)
