import re

f = open('C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q1\\input.txt', "r")
pattern = r'^\n'



data=f.read()

data=data.split("\n\n")
print(data)

currMax=[]
for i in data:
    temp=i.split('\n')
    tempmax=0
    print(temp)
    for j in temp:
        tempmax+=int(j)
    currMax.append(tempmax)
currMax.sort(reverse=True)
print(currMax[0:3])
print(67633+ 66296+ 65699)

