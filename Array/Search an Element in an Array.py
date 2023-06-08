a = [1,2,3,4,5]
k = 6
a.sort()
l=0
r= len(a) - 1
flag = 0
while l<=r:
    mid = (l+r) >> 1
    if a[mid] == k:
        print(mid)
        flag = 1
        break
    if a[mid] < k:
        l= mid + 1
    else:
        r= mid - 1

if not flag:
    print(-1)
