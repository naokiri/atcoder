n, d = map(int,input().split())

a, b = divmod(n , (d*2+1))
if b!=0:
    a=a+1
    
print("{}".format(a))
