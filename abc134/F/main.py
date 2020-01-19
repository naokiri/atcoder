def next_permutation(L):
    '''
    Permute the list L in-place to generate the next lexicographic permutation.
    Return True if such a permutation exists, else return False.
    '''
     
    n = len(L)
 
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1
     
    if i == -1:
        return False
 
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]
     
    left = i + 1
    right = n - 1
 
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
             
    return True


def oddness(L):
    ret = 0
    for i in range(len(L)):
        ret = ret + abs(L[i] - (i + 1))
    return ret


n,k = map(int,input().split())

l = list(map(lambda x: x + 1, range(n)))

if k == 0:
    print("1")
    exit(0)

ans = 0
while next_permutation(l):
    if oddness(l) == k:
        ans = ans + 1


print("{}".format(ans%(1000000007)))
