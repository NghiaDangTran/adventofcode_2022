from collections import Counter
f = open(
    'C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q6\\input.txt', "r")
data = f.read()
for i in range(len(data)):
    
    sample = Counter( data[i:i+14])
    if len(sample)==14:

        print(sample,i+14)
        break
