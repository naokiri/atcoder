import math

n = int(input())

ans = [0] * n

def baisuu(num, max):
    ret = []
    i = num
    while i <= max:
        ret.append(i)
        i = i + num
    return ret
    

# print("{}".format(baisuu(4,4)))

an = list(map(int, input().split()))

for i in range(n):
    sum = 0
    for mltp in baisuu(n-i, n):
        sum = sum+ans[mltp-1]
    if not sum % 2 == an[n-i-1]:
        ans[n-i-1] = 1
                     

ans = list(map(lambda x: x%2,ans))
print("{}".format(ans.count(1)))

for i in range(n):
    if ans[i] == 1:
        print("{}".format(i+1))

