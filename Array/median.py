a = [2,5,1,7]
a.sort()
n = len(a)
if n&1:
    print(a[n//2])
else:
    print((a[n//2 - 1] + a[n//2])/2)