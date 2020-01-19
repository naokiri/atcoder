# def trycand(first, second, nextcand):
#     rest = nextcand.copy()
#     rest.remove(second)
#     n1 = first
#     n2 = second
#     while rest:
#         try:
#             n3 = n1 ^ n2
#             rest.remove(n3)
#             n1 = n2
#             n2 = n3
#         except ValueError:
#             return False
#     return True
#
#
# n = input()
#
# a = list(map(lambda x: int(x), input().split()))
# first = a[0]
# #print(first)
# nextcand = a[1:]
# #print(nextcand)
#
# for second in nextcand:
#     if trycand(first, second, nextcand):
#         print("Yes")
#         exit()
#
# print("No")
# exit()

n = input()

a = list(map(lambda x: int(x), input().split()))

xor = 0

for i in a:
    xor = xor ^ i

if xor == 0:
    print("Yes")
else:
    print("No")
