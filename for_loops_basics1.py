for x in range(151):
    print(x)

for x in range(5,1000, 5):
    print(x)

for x in range(0, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

sum=0
for x in range(0, 500000, 2):
    Sum= x+1
    print(Sum)

sum=0
for x in range(2018, 0, -4):
    Sum= x-1
    print(Sum)

lownum = 2
highnum = 13
mult = 2
for x in range(lownum, highnum):
    if x % mult == 0:
        print(x)
