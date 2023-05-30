a = [2,5,1,3,0]
a.sort()
l = len(a)//2
r = len(a)-1
while l<r:
    a[l],a[r] = a[r],a[l]
    l+=1
    r-=1
print(a)