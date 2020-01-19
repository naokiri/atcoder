
a,b = map(int, input().split())

s = max(a-b, a+b, a*b)

print("{}".format( s))
