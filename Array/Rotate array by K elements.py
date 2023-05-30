a = [1,2,3,4,5]
d = 2
d = d%len(a)
a.sort()
l = 0
r=d-1
while l<r:
    a[l],a[r] = a[r],a[l]
    l+=1
    r-=1

l = d
r=len(a)-1
while l<r:
    a[l],a[r] = a[r],a[l]
    l+=1
    r-=1

l = 0
r = len(a)-1
while l<r:
    a[l],a[r] = a[r],a[l]
    l+=1
    r-=1
print(a)