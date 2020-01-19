n = int(input())
counter = {}
uniqs = set()
for i in range(n):
    s = list(input())
    s.sort()
    s = ''.join(s)
    counter[s] = counter.get(s,0) + 1
    uniqs.add(s)
    #print("{}".format(s[i]))

ans = 0
for orig in uniqs:
    occurence = counter.get(orig)
    ans = ans + (occurence * (occurence -1)) // 2
print("{}".format(ans))


