a = [2,5,1,3,0]
mx = a[0]
for i in a:
    if i > mx:
        mx = i
print(mx)

#method 2
a.sort()
print(a[-1])
