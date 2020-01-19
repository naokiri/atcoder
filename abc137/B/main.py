
k, x = map(int, input().split())

result = []
for i in range(-1000000,1000001):
    if x-k < i and i < x + k:
        result.append(str(i))
print("{}".format(' '.join(result)))

