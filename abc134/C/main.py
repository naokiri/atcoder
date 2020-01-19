n = int(input())

a = []
maxA = 0
secondA = 0

for i in range(n):
    a.append(int(input()))
    if a[i] > maxA:
        secondA = maxA
        maxA = a[i]
    elif a[i] > secondA:
        secondA = a[i]

for i in range(n):
    if a[i] == maxA:
        print("{}".format(secondA))
    else:
        print("{}".format(maxA))
