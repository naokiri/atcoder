n = int(input())
p = list(map(int, input().split()))

min_num = n + 1
count = 0
for i in range(n):
    if min_num > p[i]:
        min_num = p[i]
        count = count + 1
print("{}".format(count))
