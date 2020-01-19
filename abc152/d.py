n = int(input())

t = [[0 for i in range(10)] for j in range(10)]

for i in range(n):
    x=i+1
    l = x % 10
    f = x
    while f // 10 > 0:
        f = f // 10
#    print("{}: {},{}".format(i,f,l))    
    t[f][l] = t[f][l] + 1

count = 0    
for i in range(10):
    for j in range(10):        
        count = count + t[i][j] * t[j][i]             

print("{}".format(count))
