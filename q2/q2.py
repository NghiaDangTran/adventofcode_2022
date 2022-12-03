f = open('C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q2\\input.txt', "r")
data = f.read()

data = data.split("\n")
extra = {"X": 1, "Y": 2, "Z": 3}
orther = {"A": 1, "B": 2, "C": 3}

# part a
# score=0
# for i in data:
#     curr=i.split(' ')
#     score+=extra[curr[1]]
#     I=extra[curr[1]]
#     U=orther[curr[0]]
#     if (I==1 and U==3) or (I==2 and U==1) or(I==3 and U==2):
#         score+=6
#     elif U==I:
#         score+=3


# print(score)


# part b
score = 0
outCome = {"X": 0, "Y": 3, "Z": 6}
print(data)
for i in data:
    curr = i.split(' ')
    score += outCome[curr[1]]
    val = list(orther.keys())

    if curr[1] == "X":


        temp=ord(curr[0])-ord("A")-1
        if temp<0:
            temp=2

        
        print(curr[0], curr[1],orther[val[temp % 3]] ,val[temp % 3])
        score += orther[val[temp % 3]]
        # print(orther[val[ord(curr[0])-ord("A")-1 % 3]])
    if curr[1] == "Y":
        score += orther[curr[0]]
        print(curr[0], curr[1], orther[curr[0]],curr[0])
    if curr[1] == "Z":
        # print(ord(curr[0])-ord("A") +1)
        temp=ord(curr[0])-ord("A")+1
        if temp>3:
            temp=0
        print(curr[0], curr[1],orther[val[temp % 3]] ,val[temp % 3])
        score += orther[val[temp% 3]]
        # print(orther[val[ord(curr[0])-ord("A")+1 % 3]])


print(score)
