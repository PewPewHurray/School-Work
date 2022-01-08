for x in range(151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1, 101):
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)

sum=0
for x in range(500000):
    if x%2 != 0:
        sum = sum + x
    if x==499999:
        print(sum)

for x in range(2018,0,-4):
    print(x)

lowNum=2
highNum=9
for x in range(lowNum,highNum+1):
    if x%3 == 0:
        print(x)